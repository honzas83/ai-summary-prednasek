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
- Přístup k PDF skillu v Codexu a lokální nástroje pro převod a kontrolu PDF, typicky Pandoc, LaTeX a Poppler.
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
