# Specifikace studijního shrnutí

Výstup je čistý český Markdown v UTF-8 bez YAML frontmatteru, titulní strany, úvodu, závěru a poznámek o procesu kromě níže předepsaného upozornění na AI. Použij právě tři níže uvedené nadpisy první úrovně a v tomto pořadí.

## 1. Shrnutí hlavních bodů

```markdown
# Shrnutí hlavních bodů

*Upozornění: Tento dokument byl vytvořen s podporou umělé inteligence na základě slajdů a výkladu vyučujícího. Může obsahovat chyby nebo nepřesnosti. Bez doprovodných slajdů mohou být některé části nejasné nebo zavádějící.*

1. **Název tématu** - Souvislé a věcně úplné vysvětlení tématu pro studenty.

2. **Další téma** - Vysvětlení v pořadí, v jakém zaznělo na přednášce.
```

- Hned za první nadpis vlož přesné upozornění z ukázky jako jeden odstavec celý kurzívou, uzavřený do jedné dvojice hvězdiček podle ukázky. Uveď je právě jednou, před první položkou seznamu.
- Použij číslovaný seznam.
- Zahrň všechna podstatná témata aktuálního výkladu, ne každou odbočku nebo výplňovou větu.
- Každý bod začíná krátkým tučně formátovaným pojmem nebo názvem tématu.
- Dodrž chronologii přepisu. Slajdy slouží ke zpřesnění, nikoli k přeuspořádání podle jejich obsahu.
- Piš jako vyučující pro studenty, jasně a bez metakomentářů.

## 2. Co nenajdete v prezentaci

```markdown
# Co nenajdete v prezentaci

1. **Doplňující téma** - Podstatná informace z výkladu, která v aktuálních slajdech není.
```

- Použij číslovaný seznam a chronologii přepisu.
- Porovnávej s celým aktuálním PDF, nejen s názvy slajdů.
- Za chybějící nepovažuj pouhé rozvedení, příklad nebo jiné slovní vyjádření téhož bodu ze slajdů, pokud nepřináší významnou novou informaci.
- Nezahrnuj drobnou konverzaci, přeřeknutí ani osobní údaje studentů.
- Pokud žádný významný bod mimo slajdy není, napiš pod nadpis jedinou větu: `V přednášce nezazněla žádná významná témata nad rámec prezentace.`

## 3. Důležité pojmy

```markdown
# Důležité pojmy

- **API (Application Programming Interface)** - Stručná definice pojmu v kontextu přednášky.

- **Další pojem** - Srozumitelná a samostatně použitelná definice.
```

- Použij odrážkový seznam.
- Seznam má být vyčerpávající pro aktuální slajdy a důležitý obsah aktuálního výkladu.
- Řaď abecedně podle zobrazeného českého názvu nebo zkratky; nerozlišuj velikost písmen.
- Každý pojem uveď jednou. Synonyma a zkratky sluč, pokud tím neutrpí dohledatelnost.
- Definice mají být stručné, samostatně srozumitelné a odpovídat významu použitému v přednášce.

## Jazyk a typografie

- Používej spisovnou češtinu s diakritikou.
- Názvy produktů, protokolů a zkratky zachovej v oficiálním zápisu.
- Mezi tučným názvem a vysvětlením používej běžný spojovník `-`.
- Nepřidávej citace, zdrojové značky, časové kódy ani odkazy, pokud nejsou samy důležitou součástí probíraného obsahu.
- Nepřidávej žádný text mimo tři sekce.

## Povolené prvky Markdownu

- Pouze tři nadpisy první úrovně uvedené výše, v předepsaném pořadí.
- První dvě sekce používají jednoúrovňové číslované seznamy od 1, třetí odrážky `-`.
- Každá položka zabírá jeden zdrojový řádek a má přesný tvar `1. **Název** - Text` nebo `- **Pojem** - Definice`. Vysvětlení je prostý text, bez dalšího formátování.
- Mezi položkami a za nadpisy je prázdný řádek. Výjimkami ze seznamového obsahu jsou předepsané upozornění za prvním nadpisem a prostá věta pro sekci bez doplnění. Oba odstavce odděl prázdnými řádky.
- Nepoužívej další nadpisy, tabulky, vnořené seznamy, kurzívu mimo předepsané upozornění, další tučné úseky, inline kód, kódové bloky, obrázky, HTML, LaTeX, matematickou sazbu, frontmatter ani Markdown odkazy. Důležité URL mohou být prostým textem.
- Rezervované znaky pro nepovolené formátování (`*`, `_`, zpětný apostrof, `$`, `<`, `>`, `|` a zpětné lomítko) nepiš do názvů ani vysvětlení. Hvězdičky jsou povolené pouze ve vyznačení úvodního tučného názvu a kurzívy celého předepsaného upozornění. Například příkaz iptables -L piš prostě a nerovnost vyjádři slovně.

## PDF

PDF vzniká výhradně skriptem `scripts/render_summary.py` z hotového Markdownu. Pevnou sazbu určuje `assets/pdf-style.json` a přibalené fonty DejaVu Sans: A4, okraje 22 mm, základní písmo 11 bodů, řádkování 15 bodů, černý text a číslování stran. Zachovej všechny tři sekce, seznamy a tučné názvy, bez titulní strany a obsahu. Nepřidávej vlastní styl ani náhradní převodník.

Skript ověřuje formát vstupu, čitelnost PDF a přítomnost textu ve správném pořadí. Úplnost obsahu a vzhled všech stran dále ověř podle skillu `$pdf`. Změny společného vzhledu patří do skillu, ne do jednotlivého běhu.

## Volitelný DOCX

Pouze na výslovné vyžádání vzniká navíc `<název-prezentace>.summary.docx`. Obsahově se shoduje s Markdownem a PDF včetně celého upozornění kurzívou hned za prvním nadpisem. Zachovej skutečné styly nadpisů, seznamy a tučné názvy; číslování každé sekce začíná od 1. Použij stejný základní vzhled jako v PDF, bez požadavku na shodné zalomení stran. Postup vytvoření a povinné kontroly uvádí část „Volitelný DOCX“ v `SKILL.md`.
