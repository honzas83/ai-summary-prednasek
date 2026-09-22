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

## PDF

PDF vytvoř přímo z hotového Markdownu v čistém A4 rozvržení vhodném pro studium a tisk. Zachovej hierarchii nadpisů, číslování, odrážky a tučné názvy. Použij font s úplnou podporou češtiny, přiměřené okraje a číslování stran. Výsledný dokument vizuálně zkontroluj podle pravidel skillu `$pdf`.
