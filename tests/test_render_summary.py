"""Behavioral checks; run with the bundled runtime Python and unittest."""
import importlib.util
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

SCRIPT = Path(__file__).resolve().parents[1] / 'scripts/render_summary.py'
spec = importlib.util.spec_from_file_location('renderer', SCRIPT)
renderer = importlib.util.module_from_spec(spec)
spec.loader.exec_module(renderer)


def summary(prose='Příliš žluťoučký kůň úpěl ďábelské ódy. A & B.', extra=None):
    extra = renderer.EMPTY_EXTRA if extra is None else extra
    return f'# {renderer.HEADINGS[0]}\n\n1. **Síť** - {prose}\n\n# {renderer.HEADINGS[1]}\n\n{extra}\n\n# {renderer.HEADINGS[2]}\n\n- **Pojem** - Česká definice.\n'


class RendererTests(unittest.TestCase):
    def test_rejects_unsupported_markup(self):
        for markup in ['`kód`', '*kurzíva*', '**tučně**', '[odkaz](https://example.com)', '<b>HTML</b>', '$x$', 'a | b', r'\LaTeX', 'x_y']:
            with self.subTest(markup=markup), self.assertRaises(ValueError):
                renderer.parse_summary(summary(markup))

    def test_rejects_broken_structure(self):
        for text in [summary().replace('1. **', '2. **'), summary().replace('# Důležité pojmy', '# Jiný nadpis'),
                     summary() + '- **pojem** - Duplicita.\n', summary().replace('1. **Síť** - ', '    1. **Síť** - '),
                     summary().replace('Česká definice.', 'První řádek.\nPokračování.')]:
            with self.subTest(text=text), self.assertRaises(ValueError):
                renderer.parse_summary(text)

    def test_empty_extra_cannot_be_combined_with_list(self):
        with self.assertRaises(ValueError):
            renderer.parse_summary(summary(extra=renderer.EMPTY_EXTRA + '\n1. **Navíc** - Text.'))
        renderer.parse_summary(summary(extra='1. **Navíc** - Text.'))

    def test_czech_text_and_deterministic_pdf(self):
        with tempfile.TemporaryDirectory() as directory:
            blocks = renderer.parse_summary(summary())
            a, b = Path(directory) / 'a.pdf', Path(directory) / 'b.pdf'
            renderer.render(blocks, a)
            renderer.render(blocks, b)
            self.assertEqual(renderer.verify_pdf(a, blocks), 1)
            self.assertEqual(a.read_bytes(), b.read_bytes())

    def test_long_paragraph_across_pages_preserves_all_text(self):
        with tempfile.TemporaryDirectory() as directory:
            blocks = renderer.parse_summary(summary(('Dlouhý český text vysvětlující síťovou komunikaci. ' * 300).strip()))
            pdf = Path(directory) / 'long.pdf'
            renderer.render(blocks, pdf)
            self.assertGreater(renderer.verify_pdf(pdf, blocks), 1)

    def test_cli_does_not_overwrite_or_publish_invalid_input(self):
        with tempfile.TemporaryDirectory() as directory:
            md, pdf = Path(directory) / 'input.md', Path(directory) / 'output.pdf'
            md.write_text(summary(), encoding='utf-8')
            pdf.write_bytes(b'existing user file')
            result = subprocess.run([sys.executable, str(SCRIPT), str(md), str(pdf)], capture_output=True)
            self.assertNotEqual(result.returncode, 0)
            self.assertEqual(pdf.read_bytes(), b'existing user file')
            pdf.unlink()
            md.write_text(summary('`unsupported`'), encoding='utf-8')
            result = subprocess.run([sys.executable, str(SCRIPT), str(md), str(pdf)], capture_output=True)
            self.assertNotEqual(result.returncode, 0)
            self.assertFalse(pdf.exists())


if __name__ == '__main__':
    unittest.main()
