#!/usr/bin/env python3
"""Render the skill's restricted Markdown using its fixed PDF style."""
import argparse
import html
import json
from pathlib import Path
import re
import tempfile
import unicodedata

HEADINGS = ('Shrnutí hlavních bodů', 'Co nenajdete v prezentaci', 'Důležité pojmy')
EMPTY_EXTRA = 'V přednášce nezazněla žádná významná témata nad rámec prezentace.'
ASSETS = Path(__file__).resolve().parent.parent / 'assets'


def parse_summary(text):
    """Return (kind, label, title, explanation); reject unsupported syntax."""
    blocks, section, count, terms = [], -1, 0, set()
    for lineno, line in enumerate(text.splitlines(), 1):
        if not line.strip():
            continue
        if line.startswith('# '):
            if section >= 0 and not count:
                raise ValueError(f'Prázdná sekce: {HEADINGS[section]}')
            section += 1
            if section >= 3 or line != '# ' + HEADINGS[section]:
                raise ValueError(f'Řádek {lineno}: nesprávný nadpis nebo pořadí sekcí.')
            blocks.append(('heading', '', HEADINGS[section], ''))
            count = 0
            continue
        if section < 0:
            raise ValueError('Dokument musí začínat prvním předepsaným nadpisem.')
        if section == 1 and line == EMPTY_EXTRA:
            if count:
                raise ValueError('Větu o chybějících doplněních nelze kombinovat se seznamem.')
            count = 1
            blocks.append(('plain', '', line, ''))
            continue
        if section == 1 and blocks[-1][0] == 'plain':
            raise ValueError('Větu o chybějících doplněních nelze kombinovat se seznamem.')
        pattern = r'(\d+)\. \*\*([^*]+)\*\* - (.+)' if section < 2 else r'(-) \*\*([^*]+)\*\* - (.+)'
        match = re.fullmatch(pattern, line)
        if not match:
            raise ValueError(f'Řádek {lineno}: očekávám jednu položku ve tvaru číslo/odrážka, **název** - text.')
        label, title, explanation = match.groups()
        if section < 2 and int(label) != count + 1:
            raise ValueError(f'Řádek {lineno}: číslování musí postupovat od 1 bez mezer.')
        for value in (title, explanation):
            if value != value.strip() or re.search(r'[*_`$<>|\\]|\[[^\]]*\]\(|!\[', value):
                raise ValueError(f'Řádek {lineno}: nepovolené formátování; používejte prostý text.')
            if any(unicodedata.category(c) in ('Cc', 'Cf') for c in value):
                raise ValueError(f'Řádek {lineno}: nepovolený řídicí či neviditelný znak.')
        if section == 2:
            key = unicodedata.normalize('NFC', title).casefold()
            if key in terms:
                raise ValueError(f'Duplicitní pojem: {title}')
            terms.add(key)
        blocks.append(('item', label + '.' if section < 2 else '•', title, explanation))
        count += 1
    if section != 2 or not count:
        raise ValueError('Dokument musí obsahovat všechny tři neprázdné sekce.')
    return blocks


def verify_pdf(path, blocks):
    from pypdf import PdfReader
    reader = PdfReader(path)
    pages = []
    for number, page in enumerate(reader.pages, 1):
        # The renderer adds the page number as the final text object.
        text = page.extract_text().rstrip()
        if not text.endswith('\n' + str(number)):
            raise ValueError('Nelze ověřit číslování stran PDF.')
        text = text.rsplit('\n', 1)[0]
        if not text.strip():
            raise ValueError('PDF obsahuje prázdnou stranu.')
        pages.append(text)
    normalize = lambda value: re.sub(r'\s+', '', value)
    actual = normalize('\n'.join(pages))
    cursor = 0
    for kind, label, title, explanation in blocks:
        expected = title if kind != 'item' else title + ' - ' + explanation
        position = actual.find(normalize(expected), cursor)
        if position < 0:
            raise ValueError(f'V PDF chybí nebo je změněn text: {title}')
        cursor = position + len(normalize(expected))
    return len(reader.pages)


def render(blocks, output):
    from reportlab.lib import colors
    from reportlab.lib.pagesizes import A4
    from reportlab.lib.styles import ParagraphStyle
    from reportlab.lib.units import mm
    from reportlab.pdfbase import pdfmetrics
    from reportlab.pdfbase.ttfonts import TTFont
    from reportlab.platypus import SimpleDocTemplate, Paragraph, KeepTogether
    style = json.loads((ASSETS / 'pdf-style.json').read_text(encoding='utf-8'))
    if style['page'] != 'A4':
        raise ValueError('Nepodporovaný formát stránky.')
    for face, key in [('Summary', 'font_regular'), ('Summary-Bold', 'font_bold')]:
        pdfmetrics.registerFont(TTFont(face, str(ASSETS / style[key])))
    pdfmetrics.registerFontFamily('Summary', normal='Summary', bold='Summary-Bold')
    for kind, label, title, explanation in blocks:
        for face, value in [('Summary-Bold' if kind != 'plain' else 'Summary', title), ('Summary', explanation)]:
            chars = pdfmetrics.getFont(face).face.charToGlyph
            missing = [c for c in value if ord(c) not in chars]
            if missing:
                raise ValueError(f'Font nepodporuje znaky: {"".join(sorted(set(missing)))}')
    body = ParagraphStyle('body', fontName='Summary', fontSize=style['body_size_pt'],
                          leading=style['body_leading_pt'], spaceAfter=style['paragraph_space_after_pt'],
                          textColor=colors.HexColor(style['text_color']),
                          leftIndent=style['list_indent_pt'], bulletFontName='Summary',
                          bulletFontSize=style['body_size_pt'], allowWidows=0, allowOrphans=0)
    plain = ParagraphStyle('plain', parent=body, leftIndent=0)
    heading = ParagraphStyle('heading', fontName='Summary-Bold', fontSize=style['heading_size_pt'],
                             leading=style['heading_leading_pt'], spaceBefore=style['heading_space_before_pt'],
                             spaceAfter=style['heading_space_after_pt'], keepWithNext=True,
                             textColor=colors.HexColor(style['text_color']))
    story = []
    for kind, label, title, explanation in blocks:
        if kind == 'heading':
            story.append(Paragraph(html.escape(title), heading))
        elif kind == 'plain':
            story.append(Paragraph(html.escape(title), plain))
        else:
            content = '<b>' + html.escape(title) + '</b> - ' + html.escape(explanation)
            story.append(KeepTogether([Paragraph(content, body, bulletText=label)]))
    def footer(canvas, doc):
        canvas.setFont('Summary', style['footer_size_pt'])
        canvas.setFillColor(colors.HexColor(style['text_color']))
        canvas.drawCentredString(A4[0] / 2, style['footer_y_mm'] * mm, str(doc.page))
    margin = style['margin_mm'] * mm
    doc = SimpleDocTemplate(str(output), pagesize=A4, leftMargin=margin, rightMargin=margin,
                            topMargin=margin, bottomMargin=margin,
                            title='Studijní shrnutí přednášky', author='', invariant=1)
    # Render footer after body, so the verifier can remove only the page number.
    doc.build(story, onFirstPage=lambda c, d: None, onLaterPages=lambda c, d: None,
              canvasmaker=_footer_canvas(footer))


def _footer_canvas(footer):
    from reportlab.pdfgen.canvas import Canvas
    class FooterCanvas(Canvas):
        def showPage(self):
            # Page counters match the document's simple sequential pagination.
            class Page:
                page = self._pageNumber
            footer(self, Page())
            super().showPage()
    return FooterCanvas


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('input', type=Path, help='Markdown podle specifikace skillu')
    parser.add_argument('output', type=Path, help='Nový výstupní PDF soubor')
    args = parser.parse_args()
    try:
        if args.output.suffix.lower() != '.pdf':
            raise ValueError('Výstup musí mít příponu .pdf.')
        if args.output.exists():
            raise ValueError('Výstup již existuje. Použijte novou dočasnou cestu; skript nepřepisuje soubory.')
        blocks = parse_summary(args.input.read_text(encoding='utf-8'))
        with tempfile.TemporaryDirectory(prefix='lecture-pdf-') as tmp:
            pdf = Path(tmp) / 'summary.pdf'
            render(blocks, pdf)
            pages = verify_pdf(pdf, blocks)
            with args.output.open('xb') as stream:
                stream.write(pdf.read_bytes())
        print(f'PDF vytvořeno a text ověřen: {args.output} ({pages} stran)')
    except (ValueError, OSError, ImportError) as error:
        parser.exit(1, f'Chyba: {error}\n')


if __name__ == '__main__':
    main()
