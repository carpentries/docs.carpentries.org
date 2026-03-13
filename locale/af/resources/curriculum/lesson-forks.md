# Verkking van 'n werkbanklesbewaarplek

Volg hierdie stappe om jou te help om opstel te kry wanneer jy 'n lesbewaarplek op GitHub verskaf wat [The Carpentries Workbench] (https://carpentries.github.io/workbench/) gebruik.

1. [Aktiveer die GitHub Actions werkvloei] (#enable-the-github-actions-workflows)
2. [Aktiveer GitHub-bladsye] (#activate-github-pages)
3. [Stel instandhoudswerkstrome op] (#configure-maintenance-workflows)
4. [Kry hulp] (#getting-help)

## Aktiveer die GitHub-aksiewerkvloei

Aksies word standaard gedeaktiveer in gevurkbewaarde bewaarplekke.
As u wil hê dat 'n leswebwerf uit die lêers in u vurk gebou moet word, moet u dit aktiveer.
\*\* U moet dit doen voordat u GitHub-bladsye op die bewaarplek aktiveer. \*\*

1. Om GitHub-aksies in te skakel, navigeer na die oortjie _Aksie_ van u bewaarplek.
   U moet 'n knoppie vind wat sê: “Ek verstaan my werkstrome, gaan voort en aktiveer hulle” _, waarop u kan klik.
   Dit moet dan 'n bladsy vertoon met die werkstrome vir die bewaarplek aan die linkerkant.
2. Drie van die werkvloei wat in die linkerkant gelys word, is geskeduleer om weekliks te loop en sal steeds gedeaktiveer word.
   Om leswebwerfboude in te skakel, kies die werkvloei genaamd `01 Build and Deploy Site` en dan _Aktiveer werkvloei_ regs bo van die venster.
3. Om die leswebwerf-bouwerkvloei vir die eerste keer uit te voer, kies die _Begin werkvloei_ aftreklys (waar die _Aktiveer werkvloei_ -knoppie in stap 2 was) en dan die _Begin werkvloei_ knoppie.
   Die bouproses sal 'n paar minute duur, waarna die \`gh-blades'-tak van jou bewaarplek geskep/opgedateer sal word om die nuutste weergawe van die leswebwerf te bevat.
   U kan nou [GitHub Pages aktiveer] (#activate-github-pages) om die lêers in daardie tak aan die internet te bedien.
4. As u die weeklikse werkvloei wil instel wat outomaties trekversoeke kan oopmaak om die lesinfrastruktuur en pakketkas op te dateer (slegs R Markdown-lesse), moet u stap 2 hierbo herhaal vir die twee ander gedeaktigde werkstrome, genaamd `02 Maintain: Update Workflow Files` en `03 Behou: Update Package Cache`.
   Nadat die werkvloei geaktiveer is, moet u ['n paar addisionele konfigurasie voltooi, wat hieronder beskryf word] (#configure-maintenance-workflows), voordat dit suksesvol sal loop.

## Aktiveer GitHub-bladsye

\*\* Nadat u u GitHub Actions -werkvloei geaktiveer het (sien hierbo) \*\*, kan u GitHub-bladsye opstel om u leswebwerf vanaf u bewaarplek se \`gh-blades' tak te bedien.

1. Maak die oortjie _Instellings_ van u lesbewaarplek oop en navigeer dan na _Pages_ onder _Kode en outomatisering_ in die linkerkant.
2. Onder _Buu en implementering_, hou _Deploy uit 'n tak_ gekies en kies `gh-blades` uit die aftrelmenu onder _Tak_.
3. Klik op _Save _.
4. Keer terug na die voorblad (oortjie _kode_) van u lesbewaarplek en kies die ratwielsimbool regs bo van die _About_ afdeling.
   Merk die _Gebruik jou GitHub Pages-webwerf_ blokkie om die URL van die leswebwerf wat uit jou vurk gebou is, te vertoon.

## Stel onderhoudswerkstrome op

As dit toepaslik gekonfigureer is, kan die twee instandhoudswerkstrome, `02 Handhaaf: Update Workflow Files` en `03 Maintain: Update Package Cache`, trek versoeke op u bewaarplek skep om die lesinfrastruktuur te hou en (as u les R Markdown-bronlêers gebruik) die pakkette wat in die les gebruik word, op datum namate nuwe weergawes vrygestel word.
Om dit te laat werk, moet u 'n toegangsteken skep waarmee die werkvloei namens u trekversoeke kan oopmaak.

1. Maak <https://github.com/settings/tokens/new> oop en voer die naam `Sandpaper Token (<your github repository name>) `in vir jou teken, bv. `Sandpapier Token (karpentries/leson-ontwikkeling-opleiding)`
2. Kies 'n lewensduur vir die token.
   Vir veiligheid beveel ons aan dat u nie _Geen verval _ kies nie. Maar **as jy die stap hieronder volg** kan die token slegs gebruik word om 'n baie beperkte aantal take op jou bewaarplek uit te voer, dus hoef jy ook nie noodwendig 'n baie kort lewensduur te kies nie.
3. Merk die kassie onder _Kies doelple_ vir die _werkvloei_ -omvang. (Dit sal veroorsaak dat al die _repo_ -skope ook nagegaan word.)
4. Kies _Genereer token_.
5. Jou nuwe persoonlike toegangsteken sal vertoon word, met 'n knoppie langs wat gebruik kan word om die token na jou knipbord te kopieer.
   Kopieer die token en keer terug na die oortjie _Instellings_ van u lesbewaarplek.
   Onder _Sekurity_ in die linkerkant, maak die _Geheime en veranderlikes oop en kies _Aksie_.
6. Voer `SANDPAPER_WORKFLOW` as die naam in en plak jou token in die _Value_ veld.
7. Kies _Voeg geheim by _ om die konfigurasie te voltooi.

## Kry hulp

As u probleme ondervind met enige van hierdie stappe, kan u hulp vra deur:

- Plaas na die `#workbench` en/of `#lesson -dev` -kanale op Slack ({{'[Join by die Carpentries Slack werkruimte] ({}) '.format (slack_invite)}}).
- [Kontak met die kurrikulumspan per e-pos] (mailto:curriculum@carpentries.org).
- Maak 'n probleem op u bewaarplek oop, beskryf die probleem wat u teëgekom het, en merk `@tobyhodges`.

Om ander te help om jou probleem op te los, sluit asseblief 'n URL na jou gevurkbewaarplek in jou boodskap in.
