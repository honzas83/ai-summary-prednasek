# AI summary přednášek

Codex skill pro automatické zpracování nahrané přednášky a odpovídajících slajdů do studijního shrnutí v Markdownu a PDF.

Skill:

- vyhledá slajdy se stejným názvem jako nahrávka;
- upozorní na nalezenou dvojici a při nejednoznačnosti nabídne výběr;
- vytvoří český přepis pomocí [UWebASR](https://github.com/honzas83/uwebasr-skill);
- připraví chronologické shrnutí, témata mimo prezentaci a abecední slovníček;
- vytvoří `<název>.summary.md` a `<název>.summary.pdf` vedle nahrávky;
- nepřepíše existující výstupy bez potvrzení;
- po úspěšném zpracování odstraní dočasný přepis.

## Požadavky

- Codex s podporou skills.
- Nainstalovaný skill [uwebasr-client](https://github.com/honzas83/uwebasr-skill).
- Runtime Codexu s Pythonem, ReportLabem a pypdf pro převod; PDF skill a Poppler pro vizuální kontrolu. Pandoc, TeX ani systémové fonty nejsou potřeba.
- Připojení k internetu během rozpoznávání řeči službou UWebASR.

## Instalace do Codexu

Nejjednodušší je požádat Codex o instalaci z GitHubu:

```text
Použij $skill-installer a nainstaluj skill z https://github.com/honzas83/ai-summary-prednasek.
```

Stejným způsobem lze doinstalovat požadovaný UWebASR skill:

```text
Použij $skill-installer a nainstaluj skill z https://github.com/honzas83/uwebasr-skill.
```

Pro ruční uživatelskou instalaci naklonujte oba repozitáře do adresáře se skills:

```bash
mkdir -p ~/.agents/skills
git clone https://github.com/honzas83/ai-summary-prednasek.git ~/.agents/skills/ai-summary-prednasek
git clone https://github.com/honzas83/uwebasr-skill.git ~/.agents/skills/uwebasr-skill
```

Codex změny obvykle rozpozná automaticky. Pokud se skill v nabídce neobjeví, restartujte Codex.

## Příklad použití

Nahrávka a slajdy jsou uložené vedle sebe se stejným základem názvu:

```text
2026/01/ite01.mp3
2026/01/ite01.pdf
```

V Codexu zadejte:

```text
Použij $ai-summary-prednasek na 2026/01/ite01.mp3.
```

Po dokončení vzniknou:

```text
2026/01/ite01.summary.md
2026/01/ite01.summary.pdf
```

Skill na konci odpovědi přidá klikatelné odkazy na oba výsledné soubory.

Výchozím jazykem je čeština a používá se model `lindat/generic/cs/zipformer`. Jiný jazyk lze zadat přímo v požadavku:

```text
Použij $ai-summary-prednasek na recordings/lecture01.mp3. Přednáška je v angličtině.
```

## Struktura výstupu

Markdown obsahuje právě tři části:

1. `Shrnutí hlavních bodů`
2. `Co nenajdete v prezentaci`
3. `Důležité pojmy`

Ostatní přednášky v projektu slouží pouze ke kontrole terminologie a opravě zjevných chyb přepisu. Do shrnutí se nesmí dostat obsah, který není doložen aktuální nahrávkou nebo aktuálními slajdy.

## Jednotná sazba bez dalších instalací

Všechny přednášky používají jediný renderer `scripts/render_summary.py`, společný styl `assets/pdf-style.json` a přibalené fonty DejaVu Sans. PDF má A4, okraje 22 mm, černý text, základní písmo 11 bodů a čísla stran, bez titulní strany a obsahu. Licence fontů je v `assets/fonts/LICENSE.txt`.

Použijte Python poskytovaný nástrojem Codex `load_workspace_dependencies`:

```text
<RUNTIME_PYTHON> <SKILL_DIR>/scripts/render_summary.py prednaska.summary.md nove-summary.pdf
```

Skript odmítne existující cílový soubor. Pro povolenou náhradu nejprve vytvořte a vizuálně ověřte nové PDF pod dočasným názvem. Při chybě převodu nevzniká alternativně stylovaný dokument.

Markdown má omezený formát: tři předepsané nadpisy, číslované seznamy či odrážky a pouze úvodní tučný název položky. Každá položka je jeden řádek, další formátování, tabulky, kód, matematická sazba a Markdown odkazy nejsou povolené. Přesná pravidla uvádí [specifikace výstupu](references/specifikace-vystupu.md).

Renderer lze ověřit pomocí standardního unittest ze stejného runtime:

```text
<RUNTIME_PYTHON> -m unittest discover -s tests -v
```
