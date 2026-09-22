---
name: ai-summary-prednasek
description: Zpracuje nahrávku přednášky spolu s odpovídajícími slajdy v PDF do českého studijního shrnutí v Markdownu a PDF. Použij, když uživatel zadá soubor s nahrávkou a chce automatický přepis, shrnutí výkladu, témata mimo slajdy a slovníček pojmů.
---

# AI summary přednášek

Vstupem je cesta k jednomu souboru s nahrávkou. Výstupem jsou vedle něj dva soubory se stejným základem názvu: `<název>.summary.md` a `<název>.summary.pdf`. Přepis je pouze dočasný pracovní podklad.

Před zpracováním přečti [specifikaci výstupu](references/specifikace-vystupu.md). Pro rozpoznání řeči načti a dodržuj skill `$uwebasr-client`; API ani klienta neimplementuj znovu. Pro vytvoření a vizuální kontrolu PDF načti a dodržuj skill `$pdf`.

## Vstupy a ochrana existujících souborů

1. Ověř, že zadaná nahrávka existuje a je soubor.
2. Ve stejné složce nejprve hledej PDF se shodným základem názvu bez ohledu na velikost písmen, například `ite01.mp3` a `ite01.pdf`. Nikdy jako slajdy nevybírej `*.summary.pdf`.
3. Nalezené slajdy vždy oznam uživateli před spuštěním přepisu. Pokud neexistuje právě jedna jednoznačná shoda, nabídni uživateli nalezené PDF jako varianty a vyžádej si výběr; bez potvrzených slajdů nepokračuj.
4. Před drahým zpracováním zkontroluj oba cílové výstupy. Pokud alespoň jeden existuje, sděl přesné cesty a vyžádej si souhlas s přepsáním. Bez výslovného souhlasu nic nepřepisuj.
5. Při povoleném přepsání připrav nové výstupy pod dočasnými názvy a nahraď původní soubory až po úspěšném ověření nové dvojice. Neodstraňuj staré výstupy předem.

## Přepis

- Výchozí jazyk je čeština a výchozí model UWebASR je `lindat/generic/cs/zipformer`. Pokud uživatel uvede jiný jazyk, vyber odpovídající model podle `$uwebasr-client`.
- Vyžádej si jen textový výstup (`--format txt`) a směruj jej do nového dočasného adresáře, nikdy vedle nahrávky. Nepoužívej `--overwrite` na uživatelských souborech.
- Přepis považuj za nedokonalý zdroj. Opravuj zjevné chyby pomocí aktuálních slajdů a kontextu kurzu, ale nevytvářej opravený úplný přepis jako další výstup.
- Dočasný přepis a další dočasné kopie odstraň po ověření výstupů. Při chybě je nenechávej v adresáři přednášky a při ukončení práce je rovněž ukliď.

## Syntéza obsahu

Zpracuj celý přepis i celé PDF slajdů. Zachovej chronologii aktuální přednášky a piš jako vyučující pro studenty.

Ostatní přednášky v projektu smíš použít pouze k opravě názvů, ustálení terminologie a rozpoznání zjevných chyb ASR. Nepřebírej z nich témata, fakta, příklady ani organizační informace, které nejsou doloženy aktuálním přepisem nebo aktuálními slajdy. Při konfliktu mají aktuální podklady přednost.

Rozlišuj zdroje:

- shrnutí hlavních bodů pokrývá témata doložená přepisem a může je zpřesnit podle slajdů;
- část o obsahu mimo prezentaci obsahuje jen významné body doložené přepisem, které v aktuálních slajdech skutečně chybí;
- slovníček zahrnuje důležité pojmy z aktuálních slajdů i přepisu.

Neuváděj domněnky jako fakta. Nejasný název raději ověř v aktuálních slajdech nebo v kontextových materiálech; pokud jej nelze spolehlivě určit, formulaci zobecni nebo vynech.

## Výstupy a ověření

Vytvoř jediný Markdown přesně podle specifikace a z něj odvoď PDF. PDF nesmí obsahově rozšiřovat ani zkracovat Markdown.

Před předáním ověř:

- přesné názvy, pořadí a jediný výskyt všech tří sekcí;
- chronologické řazení prvních dvou číslovaných seznamů;
- abecední řazení slovníčku bez zjevných duplicit;
- že část „Co nenajdete v prezentaci“ neparafrázuje body, které už slajdy obsahují;
- že se do výsledku nedostal obsah pouze z jiné přednášky;
- shodu cílových názvů a existenci obou souborů;
- úspěšné otevření PDF, úplnost textu a vizuální render všech stran bez přetečení, ořezání, rozbitých znaků nebo prázdných stran.

Na závěr stručně uveď použité slajdy, potvrď odstranění dočasného přepisu a přidej dva klikatelné Markdown odkazy s absolutními cestami: jeden na hotový `.summary.md` a druhý na hotový `.summary.pdf`.
