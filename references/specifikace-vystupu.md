# Specifikace studijního shrnutí

Výstup je čistý český Markdown v UTF-8 bez YAML frontmatteru, titulní strany, úvodu, závěru a poznámek o procesu. Použij právě tři níže uvedené nadpisy první úrovně a v tomto pořadí.

## 1. Shrnutí hlavních bodů

```markdown
# Shrnutí hlavních bodů

1. **Název tématu** - Souvislé a věcně úplné vysvětlení tématu pro studenty.

2. **Další téma** - Vysvětlení v pořadí, v jakém zaznělo na přednášce.
```

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
- Mezi položkami a za nadpisy je prázdný řádek. Výjimkou je předepsaná prostá věta pro sekci bez doplnění.
- Nepoužívej další nadpisy, tabulky, vnořené seznamy, kurzívu, další tučné úseky, inline kód, kódové bloky, obrázky, HTML, LaTeX, matematickou sazbu, frontmatter ani Markdown odkazy. Důležité URL mohou být prostým textem.
- Rezervované znaky pro nepovolené formátování (`*`, `_`, zpětný apostrof, `$`, `<`, `>`, `|` a zpětné lomítko) nepiš do názvů ani vysvětlení. Hvězdičky jsou povolené pouze ve vyznačení úvodního tučného názvu. Například příkaz iptables -L piš prostě a nerovnost vyjádři slovně.

## PDF

PDF vzniká výhradně skriptem `scripts/render_summary.py` z hotového Markdownu. Pevnou sazbu určuje `assets/pdf-style.json` a přibalené fonty DejaVu Sans: A4, okraje 22 mm, základní písmo 11 bodů, řádkování 15 bodů, černý text a číslování stran. Zachovej všechny tři sekce, seznamy a tučné názvy, bez titulní strany a obsahu. Nepřidávej vlastní styl ani náhradní převodník.

Skript ověřuje formát vstupu, čitelnost PDF a přítomnost textu ve správném pořadí. Úplnost obsahu a vzhled všech stran dále ověř podle skillu `$pdf`. Změny společného vzhledu patří do skillu, ne do jednotlivého běhu.
