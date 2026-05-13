# Die lewensiklus van lesse

\*\*'N Nota oor _instruktors_ en _instruktors_: \*\* in die meeste van hierdie handboek verwys ons na Instrukteurs, met hoofgrootte om aan te dui dat dit 'n gesertifiseerde rol binne die gemeenskap is, dit wil sê iemand wat Carpentries Instruktoropleiding voltooi het.
Sommige van ons handboekinhoud oor kurrikulumontwikkeling verwys na instrukteurs (sonder hoofkapitaal), om te onderskei tussen diegene wat 'n werkswinkel onderrig, maar dalk nog nie gesertifiseerde instrukteurs is nie.

Die Carpentries-gemeenskap ontwikkel lesse as Open Source projekte: lesse en hul bronlêers is gewoonlik aanlyn beskikbaar vanaf die vroegste stadiums van ontwikkeling.
Dit kan nuttig wees vir besoekers aan 'n les - instrukteurs wat dit oorweeg om dit te onderrig, potensiële bydraers wat die inhoud daarvan ondersoek, ens. - en die ontwikkelaars daarvan self, om vinnig die ontwikkelingstatus van 'n les te kan identifiseer.
Lesontwikkeling is 'n iteratiewe proses, met inhoud en ontwerp wat altyd onderhewig is aan evolusie en verbetering.
Byvoorbeeld, aangesien terugvoer ontvang word wanneer 'n nuwe les geleer word, of in reaksie op nuwe funksies en ander verskuiwings in die onderwerp daarvan.
Met verloop van tyd word inhoud gewoonlik meer volledig, akkuraat, impak en stabiel, met veranderinge - veral groot wysigings soos herorganisasie of die byvoeging/verwydering van hele afdelings - minder gereeld raak.

Die Carpentries benoem die ontwikkelingstatus van lesse in 'n soortgelyke stelsel as dié wat in sagteware-ontwikkeling gebruik word: ons kategoriseer hulle volgens hul volwassenheid/stabiliteit, wat wissel van _pre-alpha_ tot _stable_.

! [Die Carpentries-les lewensiklusmodel] (../../img/life_cycle.svg)

- **_Pre-alpha:_** die les is in die aanvanklike stadiums van ontwerp en ontwikkeling.
  Die inhoud van lesse in pre-alfa sal waarskynlik onvolledig en ongetoets wees, en kan te eniger tyd groot veranderinge ondergaan. Hierdie etiket word gewoonlik op 'n les toegepas totdat 'n eerste konsep voltooi is.
- **_Alpha: _** die les word deur sy ontwikkelaars bestuur.
  Die inhoud van lesse in alfa is waarskynlik ten volle opgestel, maar sommige gapings, teenstrydighede en foute kan verwag word.
  Hierdie etiket word gewoonlik toegepas op 'n les nadat die eerste konsep daarvan voltooi is, en voordat die eerste vlieënerwerkswinkels plaasvind.
- **_Beta:_** die les is gereed om deur ander instrukteurs beheer te word.
  Die inhoud van lesse in beta is getoets deur (ten minste) sy ontwikkelaars, en die inhoud is aangepas op grond van daardie ervaring.
  Die inhoud bevat leiding vir instrukteurs oor hoe om dit effektief te leer.
  Verdere veranderinge is waarskynlik, aangesien terugvoer opgeneem word uit addisionele vlieënier
  Hierdie etiket word gewoonlik toegepas op 'n les wanneer die ontwikkelaars daarvan vol vertroue is dat dit gereed is om in werkswinkels deur ander instrukteurs gebruik te word.
- **_Stable:_**: die les het uitgebreide toetsing ondergaan en groot veranderinge word nie verwag nie (sonder beduidende waarskuwing).
  Die inhoud van stabiele lesse sal steeds van tyd tot tyd verander, maar die veranderinge is gewoonlik klein en beïnvloed nie 'n instrukteur se vermoë om dit te leer as hulle vertroud is met 'n vroeëre (stabiele) weergawe nie.
  Hierdie etiket word gewoonlik toegepas op 'n les nadat terugvoer van beta-piloetwerkswinkels opgeneem is.

Die lewensiklusstadium van 'n les word prominent aan die bokant van die bladsy op leswebwerwe vertoon.
Dit is ook sigbaar as 'n 'onderwerp' op die GitHub-bewaarplek van die les, onder die _About_ blokkie aan die regterkant van die bewaarplek tuisblad.

## Hoe word die lewensiklusstadium ingestel?

Die lewensiklusstatus van 'n les kan aangepas word deur die `life_cycle'-parameter in die les se `config.yaml\` -lêer te verander, sowel as die ekwivalente onderwerp op die bron GitHub-bewaarplek.

## Wie is verantwoordelik vir die keuse van die lewensiklusstadium van 'n les?

Vir lesse wat in die gemeenskap besit word in The Carpentries Incubator, kan lesontwikkelaars vry kies watter etiket hulle geskik is.
Lesse in die gemeenskap in The Carpentries Lab het ewekniebeoordeling geslaag en moet stabiel gemerk word.
Die lewensiklusstadium van lesse wat aan 'n Carpentries-lesprogram behoort, moet verander word na konsultasie met die betrokke kurrikulumadvieskomitee en/of die kurrikulumspan.
Konsultasie is veral belangrik voordat u 'n les as beta of stabiel merk word.

## Wat gebeur in elke stadium van die lewensiklus?

[Vlieëderwerkswinkels] (lesson-pilots.md) is waarskynlik die belangrikste gebeurtenisse wat plaasvind voordat 'n les stabiliteit bereik.
Hier is egter 'n paar ander aksies wat lesontwikkelaars in verskillende stadiums kan neem:

- \*\*Pre-alfa: \*\*
  - [Dien die les in by The Carpentries Incubator] (https://github.com/carpentries-incubator/proposals/).
  - Sluit aan by [Samewerkende Lesontwikkelingsopleiding] (https://carpentries.org/lesson-development-training).
  - Bel vir medewerkers.
  - As u die nuwe les van plan is om by 'n bestaande Carpentries-kurrikulum of lesprogram aan te sluit, raadpleeg die relevante [Kurrikulumadvieskomitee] (https://carpentries.org/curriculum-advisors/) of [Lesprogrambestuurskomitee] (https://carpentries.org/community/lesson_program_governors/) so vroeg as moontlik.
    Hierdie gemeenskapsbestuursgroepe kan terugvoer gee oor u planne en leiding bied oor hoe om suksesvolle integrasie van die nuwe les te verseker.
- \*\*Alfa: \*\*
  - Voer [alpha pilot werkswinkels] (lesson-pilots.md#alpha-and-beta-pilots) uit en herhaal die ontwerp en inhoud van die les.
  - Verhoog bewustheid van die les in The Carpentries -gemeenskap.
- \*\*Beta: \*\*
  - Soek instrukteurs wat die les kan leer in [beta pilot werkswinkels] (lesson-pilots.md#alpha-and-beta-pilots), en versamel terugvoer van hulle om die les verder te verbeter.
    Oorweeg dit om daardie [beta-vlieënige instrukteurs] (./lesson-development-roles.md#beta-pilot-instructors) te nooi om by die span aan te sluit wat die les ontwikkel/handhaaf.
  - [Publiseer die les aan Zenodo en verkry 'n DOI] (./lesson-release.md).
  - [Dien die les in vir ewekniebeoordeling in The Carpentries Lab] (https://github.com/carpentries-lab/reviews/).
- \*\* Stabiel: \*\*
  - [Laat die stabiele weergawe vry na Zenodo] (./lesson-release.md).
    - U wil hierdie proses gereeld herhaal, bv. jaarlikse vrystellings maak.

! [Die Carpentries-leslewensiklusmodel geannoteer om meer besonderhede te wys oor wat in elke stadium van die proses kan gebeur] (../../img/life_cycle_annotated.svg)
