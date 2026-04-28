# Onderhoudshandboek

## Oor hierdie handboek

Die Maintainers Handbook is ontwerp om lede van The
Carpentries -gemeenskap te ondersteun wat as 'n lesonderhouder dien. Dit word onderhou deur The Carpentries Curriculum Team.  As u glo dat iets hier bygevoeg of opgedateer moet word, of as u terugvoer oor die inhoud wil gee, stuur asseblief e-pos aan die {{'[Curriculum Team] (mailto:{}) '.format (curriculum_email)}} of maak 'n probleem op die {{' [bronbewaarplek van hierdie handboek] ({}) '.format (gh_repo)}} oop. As u onvertroud is met enige van die terme wat in hierdie handboek gebruik word, verwys asseblief na ons {{'[Woordelys van terme] ({}) '.format (woordelys)}}.

## Inleiding

Die Carpentries Maintainers werk saam met die gemeenskap om te verseker dat
lesse op datum, akkuraat, funksioneel en samehangend bly. Onderhouers
monitor hul lesbewaarplek, verseker dat trekversoeke en kwessies
betyds aangespreek word, en neem deel aan die les
-ontwikkelingsiklus, insluitend lesvrystellings. Hulle poog om
verwelkomend te wees en ondersteun vir bydraes van alle lede van die
-gemeenskap. Hierdie praktykgemeenskap is 'n wonderlike plek om te leer om
effektief saam te werk in Git en GitHub.

## Rolle en verantwoordelikhe

Die Carpentries leer elke jaar 400-600 werkswinkels, wat beteken dat ons les
-materiaal feitlik elke dag gebruik word vir sinchrone, geleide
leer. Om seker te maak dat ons lesse aanhou werk sonder onderbrekings is
, daarom is ons nommer een doel vir onderhoud.

'N Sekondêre (maar steeds uiters belangrik!) doel is om te verseker dat die
-ruimtes wat ons gebruik vir lesontwikkeling en instandhouding net so
verwelkomend en inklusief is as ons werkswinkels.

Om te verseker dat ons lesse op die voorpunt is van nuwe tegnologie en
gereedskap is nie\* 'n prioriteit vir The Carpentries nie. Alhoewel ons wel wil hê dat ons
-materiaal relevant moet bly, is dit baie belangriker dat ons lesse
pedagogies gesond en tegnies lewensvatbaar bly, as dat dit
die nuutste en grootste nuwe ontwikkelings op die veld verteenwoordig.

Met hierdie doelwitte in gedagte is die Carpentries se verwagtinge van Onderhouders
om:

- Monitor die lesbewaarplek en maak seker dat terugversoeke (PR's) en probleme onmiddellik gereageer word (selfs al is die antwoord “jammer, dit is buite die omvang”).
- Moenie nuwe foute in die les invoer nie.
- Maak vinnig alles reg wat ondubbelsinnig 'n fout is of wat werkswinkelleerders negatief beïnvloed.
- Wees ontvanklik en verwelkomend vir voorstelle vir die verbetering van die lesse.
- Evalueer alle bydraes gegewe die Carpentries -pedagogiese model:
  - Leer wat die belangrikste en nuttigste is vir leerders.
  - Vermy onnodige jargon en gedetailleerde verduidelikings. Vra altyd jouself af
    of dit nodig is vir die leerder.
  - Hou taal motiverend.
  - Ontmoet leerders waar hulle is.
  - Beklemtoon die belangrikheid van voortgesette leer en verbetering.

Onderhouders is verantwoordelik vir:

- Gewoonlik:
  - Verseker redelike reaksietyd op alle ingedien kwessies en PR's. Ten minste verseker dat alle kwessies en PR's binne twee dae erken word.
  - Aanspreek probleme vinnig aan en PR's wat as “bug” gemerk is.
  - Die indiening van kwessies soos dit ontstaan.
  - Voldoen aan die gedragskode en die gedragskomitee in waarsku oor moontlike oortredings.
  - Identifisering van potensiële nuwe onderhouders op grond van hul hersieningsaktiwiteit.

- Periodiek:
  - Help om lesse voor te berei vir publikasie.

Onderhouders verteenwoordig The Carpentries -gemeenskap en moet daarna streef om
die Carpentries-filosofie te beliggaam deur:

- Erkenning van die belangrikheid van kommunikasie en verwelkomend wees vir
  alle bydraers.

- Gee terugvoer aan bydraers met behulp van The Carpentries-model:

  - Vind wat goed is.
  - Wees spesifiek oor verbeterings wat nodig is.
  - Use motivating language.

- Evaluering van lesbydraes in die lig van Carpentries -pedagogiese model:

## Onboord

Nuwe onderhouders gaan deur 'n inboordproses, gelei deur 'n lid van The Carpentries Curriculum Team en die Maintainer Community Lead. Onboarding van onderhoud vind ten minste een keer per jaar plaas. Nuwe rondes van onboarding sal aangekondig word op The Carpentries-blog en die belangrikste
kommunikasiekanale (bespreking@ op TopicBox, #general Slack-kanaal).

Die kurrikulum vir die aansluiting van nuwe Onderhouders is beskikbaar as 'n {{'[Maintainer Onboarding Lesson] ({}) '.format (maintainer_onboarding)}}.

## Afboording

'N Jaarlikse e-pos met 'n opname met een vraag sal middel tot einde Januarie in
aan Onderhouers gestuur word. As die Onderhouder “ja” op hierdie opname reageer,
sal hulle 'n Onderhouder vir die volgende jaar bly. As 'n Onderhouder
“nee” antwoord of nie binne 'n maand na ontvangs van die opname reageer nie, sal hulle
'n alumnus Onderhouder word en hul toestemmings vir hul
-bewaarplek sal herroep word. Aktiewe Onderhouderstatus kan enige tyd by
herstel word deur die Maintainer Community Lead te kontak.
As 'n Onderhouder van
die rol buite hierdie skedule wil wegstap, moet hulle die Onderhouder
Community Lead en die ander Onderhouders oor hul les (s) in kennis stel.

## Kommunikasie- en samewerkings

### Slap

{{'[Sluit aan by die Carpentries Slack werkruimte] ({}) '.format (slack_invite)}}. Om gesprekke wat relevant is vir hierdie rol te volg, moet u by die volgende kanale aansluit:

- {{'[Die uitnodigings-slegs #maintainers -kanaal] ({}/archives/C8H5LN44V) '.format (slack)}} op The Carpentries Slack werkruimte is 'n platform vir die hele gemeenskap om vrae te stel en in besprekings oor die onderwerp van lesinstandhouding deel te neem. If you are a Maintainer and do not already have access to this channel, please contact the [Curriculum Team](mailto:curriculum@carpentries.org).
- Ons beveel aan dat Lesonderhouders deur bestaande kanale in die Slack-werkruimte blaai, vir enige wat relevant is vir die onderwerp/domein van hul les.
- Dit kan ook nuttig wees om 'n nuwe kanaal vir u les te skep, as 'n ruimte vir u om die ontwikkelingsproses met medewerkers te bespreek, en vir gemeenskapslede om vrae oor die les te stel.

As jy nuut is by Slack, kyk asseblief na ons {{"[Slack Guide] ({})” .format (slack_guide)}}.

### Gemeenskapskalender

Maintainer monthly calls are listed on our
{{'[Community Calendar]({}/community/events/)'.format(carpentries_website)}}. If you are planning to attend an upcoming meeting, please [register in Pretix](https://pretix.carpentries.org/lesson-maintainers/lesson-maintainers-meetings/).
Pretix will automatically calculate the event time in your local time zone and will send you a calendar invite and event reminders.

### Samewerkende notas

Die Carpentries gebruik [Etherpad] (/resources/communications/etherpads.md) as 'n samewerkende notuingsinstrument tydens werkswinkels, opleiding en ander Carpentries-verwante geleenthede.  Hieronder is 'n lys van Etherpads wat relevant is om as lesonderhouder te dien.

- {{'[Pad-of-pads] ({}/pad-of-pads) '.format (etherpad)}}: 'n Lys van
  ons mees gebruikte Etherpads en ander hulpbronne.
- {{'[Maintainer Community Oproepnots] ({}/maintainers) '.format (codimd)}}: Inskrywingsinligting, verbindingbesonderhede en aantekeninge geneem uit maandelikse coworksessies (CodimD).

### GitHub

- [Maintainer Resources](https://github.com/carpentries/maintainer-resources):  a place to read minutes from the Maintainer Community Calls and helpful tips on flight rules.

### Onderwerpaksie

U kan toegang tot The Carpentries -poslyste verkry vanaf
{{'[Topicbox] ({}/latest) '.format (topicbox)}}. Below is a list
of those most relevant to Maintainers.

- {{'[The Maintainers -poslys] ({}/groups/maintainers) '.format (topicbox)}} word gebruik vir aankondigings wat relevant is vir lesonderhouders.

Om by een of meer Carpentries-poslyste aan te sluit, moet u {{'[skep 'n aanmelding] ({}/latest) '.format (topicbox)}}. Sodra u
dit gedoen het, kan u deur die lys van groepe blaai en op
klik “Sluit aan by die gesprek” (vir oop pos) of “Versoek om aan te sluit” (vir
die poslyste wat administrateur goedkeuring vereis).  As jy nuut is by Topicbox, kyk asseblief na ons {{"[Topicbox Guide] ({})” .format (topicbox_guide)}}.

## Stap-vir-stap

### Gebruik uitgawe-etikette om samewerking te

GitHub laat die onderhouders van 'n bewaarplek toe om kontekstuele
-inligting by Issues and Pull Versoeke in die vorm van etikette te voeg.
[The Carpentries gebruik 'n uitgebreide stel uitgaweetikette op sy lesbewaarplekke] (../resources/curriculum/issue-labels.md).

Twee etikette, wat deur The Carpentries en in baie bewaarplekke regoor GitHub gebruik word, kan
ontplooi word om die sigbaarheid van u les te verhoog en
-gemeenskapslede aan te moedig om by te dra tot die ontwikkeling daarvan.

Die \*\* “help wou” \*\* etiket moet gebruik word om probleme met
uit te lig wat u bykomende hulp sal verwelkom. Soms wil u dalk die proses aktiveer voor die volgende geskeduleerde uitloop, bv. as die nuwe weergawe van die werkstrome of pakkette 'n probleem oplos wat verhoed dat u les bou. Vind uit hoe
kwessies uit u lesbewaarplek op die Help Wanted -bladsy kan insluit deur
die {{'[inligting vir onderhouders] ({}/lessons/help_wanted#information-for-maintainers) '.format (carpentries_website)}}
op die bladsy self te lees.

Die \*\* “goeie eerste uitgawe” \*\* etiket moet gebruik word om kwessies te identifiseer wat
'n goeie toegangspunt sal maak vir nuwelinge wat soek na 'n manier om
tot u les by te dra. Die werk wat nodig is om 'n probleem met hierdie
-etiket te sluit, vereis gewoonlik nie 'n uitgebreide kennis van die
-struktuur of ingewikkeldhede van u lesbewaarplek, of 'n kundige
-begrip van die inhoud nie. Die etiket “goeie eerste uitgawe” word so
groot gebruik dat GitHub 'n bladsy verskaf by `[repository
URL] /bydrae` (voorbeeld: <https://github.com/swcarpentry/r-novice-gapminder/contribute>) vir elke bewaarplek, wat probleme met hierdie etiket lys.

### Inlig gemeenskapslede oor 'n tydperk van afwesigheid

If you plan to temporarily step away from the role of Maintainer,
e.g. parental leave, exam season, etc, it can be helpful to your fellow
Maintainers and potential contributors to let them know. Hier is
'n paar stappe wat u kan neem om die gemeenskap in kennis te stel oor u tydelike
afwesigheid/onbeskikbaarheid:

1. Stel 'n status in en merk jouself as “besig” op GitHub:

   1. Meld aan by Github.com
   2. Klik op jou profielfoto regs bo van die venster
   3. Kies “Stel status”
   4. In die “Wat gebeur?” boks, skryf 'n kort verklaring waarmee
      ander gebruikers kan weet dat u nie beskikbaar is nie. U hoef nie
      mense te vertel hoekom nie - u status kan “tydelik nie beskikbaar nie” of
      “beskikbaar tot DATUM nie” wees om mense te vertel wanneer hulle kan verwag om u weer op GitHub te vind.
      Jy kan 'n emoji kies om jou
      -status te vergesel deur op die gesigsikoon langs die statusboodskap
      -invoer te klik.
   5. Merk die blokkie “Besig”, sodat ander gebruikers 'n
      -kennisgewing van GitHub oor u status sal ontvang wanneer hulle u
      noem in kwessies en versoeke trek, u aan 'n probleem toeken of 'n
      -resensie van u versoek.
   6. {{"[**Jy kan ook 'n status op Slack**] ({})” .format (slack_guide)}} instel. Die proses is baie soortgelyk aan GitHub, dit wil sê jy moet aanmeld, klik op jou profielfoto regs bo van die venster en kies “Opdateer jou status”. Dit sal 'n pop-up oopmaak waar u 'n statusboodskap kan skryf.

2. Stel jou mede-onderhouders in:

   7. Stuur vir hulle 'n e-pos of 'n direkte boodskap op Slack.
   8. If you need help finding contact information for any of your
      fellow Maintainers, contact the [Curriculum Team](mailto:curriculum@carpentries.org).

## Hulpbronne

### [Onderhouderhouderingskurrikulum] (https://carpentries.github.io/maintainer-onboarding/)

Die kurrikulum wat by Maintainer Onboarding gebruik word. Hierdie hulpbron kan 'n
nuttige verwysing wees vir Onderhouders nadat hulle die aansluiting voltooi het. It includes [tips for managing issues on a repository](https://carpentries.github.io/maintainer-onboarding/03-communicate-contributors#top-ten-tips-for-managing-issues-and-prs), guidance for [tagging the Curriculum Team on issues and pull requests](https://carpentries.github.io/maintainer-onboarding/02-communicate-maintainers.html#github), and plenty of other useful information you might want to return to after onboarding.

### [Inleiding tot The Carpentries Workbench] (https://carpentries.github.io/sandpaper-docs/)

Dokumentasie vir The Carpentries Workbench, oopbroninfrastruktuur
vir leswebwerwe. The documentation explains how to install the
Workbench so that Maintainers can edit and preview their lessons
on their computer, how to initialise a new lesson and use the
various elements of the lesson template, and how to keep up to date with
the latest changes to the infrastructure.

### [Konsultasierubriek vir kurrikulumadvieskomitee] (/handbooks/curriculum_advisors.md#curriculum-advisory-committee-consultation-rubric)

Hierdie rubriek definieer die verdeling van verantwoordelikhede tussen The
Carpentries Maintainers en The Carpentries Curriculum Advisory
Committees (CACs). Dit kan deur Onderhouders gebruik word om
te help bepaal of hulle die relevante CAC in kennis stel of te vra oor 'n voorgestelde verandering aan
hul les.

### [Lessprint-aanbevelings] (/resources/curriculum/lesson-sprint-recommendations.md)

'N Versameling aanbevelings vir gemeenskapslede wat geleenthede wil organiseer wat toegewy is aan die ontwikkeling en verbetering van 'n les. Sluit lyste in van dinge wat u moet oorweeg om voor, tydens en na 'n ontwikkelingssprint te doen, en gereedskap en ander hulpbronne om die sukses daarvan te ondersteun.

### [Lesvrylating proses] (/resources/curriculum/lesson-release.md)

'N Beskrywing van hoe om 'n lesvrystelling voor te berei en dit aan Zenodo te publiseer.
**Let daarop dat onderhouders van datammerwerk-, biblioteektimmerwerk- en sagtewarestuurlesse vir nou nie lesvrystellings moet maak nie.**
Die kurrikulumspan sal hierdie proses in die komende maande koördineer.

### [Samewerkende lesontwikkelingsopleidingskurrikulum] (https://carpentries.github.io/lesson-development-training/)

'N Les wat ontwerp is om vaardighede en goeie praktyke in lesontwerp,
leswebwerf-ontwikkeling en samewerking via GitHub te leer. Die dokumentasie verduidelik hoe om die
Workbench te installeer sodat lesonderhouders hul lesse
op hul rekenaar kan wysig en voorskou, hoe om 'n nuwe les te inisialiseer en die
verskillende elemente van die lessjabloon te gebruik, en hoe om op hoogte te bly van
die nuutste veranderinge aan die infrastruktuur.

## FAQ

### Wanneer moet ek my eie trekversoek saamvoeg?

Oor die algemeen beveel ons aan dat Onderhouders wag vir 'n goedkeurende hersiening voordat enige trekversoek saamgesmelt word.
However, if the changes are small and fix something that is unquestionably broken in the lesson -- e.g. a broken link, some malformed syntax, or similar -- then you can merge your own changes right away.

#### Wat om te doen as ander onderhouders nie reageer nie?

Soms wil 'n Onderhouder dalk 'n tweede mening van hul mede-onderhouders hê voordat hy 'n trekversoek saamsmelt (of wil dalk hê dat iemand anders hul eie veranderinge moet hersien).
Die tabel hieronder beskryf die stappe wat ons aanbeveel om te neem as u u mede-onderhouders gemerk het en 'n kort rukkie gewag het, bv. een of twee weke, maar geen antwoord ontvang het nie.

! [Tabel aanbeveel aksie wat 'n Onderhouder moet neem as hulle insette van hul mede-onderhouders op 'n trekversoek gevra het, maar geen antwoord ontvang het nadat hulle 'n geruime tyd gewag het nie. Nie dringend nie, nie kompleks nie: wag langer of merk die onderhoudse gemeenskapsleid of kurrikulumspan. Dringende, nie kompleks nie: smelt nou saam. Nie dringend nie, kompleks nie: wag langer of merk die onderhoudse gemeenskapsleid of kurrikulumspan. Dringende, kompleks: merk die onderhoudsgemeenskapsleid of kurrikulumspan.] (../img/when-to-merge.svg)

- Wat is dringend? Oor die algemeen kan u die verandering dringend beskou as die huidige weergawe van die relevante inhoud in die les verkeerd of op een of ander manier gebreek is.
  Dringende veranderinge kan tydsensitief wees (bv. 'n taalfunksie word verouderd) of sal 'n beduidende verbetering bied aan die toeganklikheid van die lesinhoud (bv. die byvoeging of verbetering van alternatiewe teks op 'n beeld).
- Wat is kompleks? Hier verwys ons na veranderinge as kompleks as dit enigiets bevat waarmee u redelik kan verwag dat iemand nie saamstem nie of anders wil woord.
  Nie-komplekse veranderinge kan tikfoutoplossings wees, opdaterings van die uitvoer van 'n voorbeeldkodeblok of 'n nuwe weergawe van 'n skermkiekie wat in die les gebruik word.

### Wanneer en hoe moet ek iemand se onvoltooide bydrae oorneem?

Dit is algemeen in oopbronprojekte dat gemeenskapslede aan iets begin werk, maar om tyd uit te loop of afgelei te raak voordat hulle klaar is.
Een resultaat kan oop, maar onvolledige trekversoeke wees, bv. gemerk as 'n konsep, of met beoordelaarkommentaar/voorgestelde veranderinge wat onaangespreek gelaat word.
'N Ander is probleemdrade waarop iemand gereageer het, wat aandui dat hulle van plan is om dit reg te stel, maar dat sedertdien geen trekversoek van hulle verskyn het nie.

Although originating from a place of good intentions, these behaviours can have the unfortunate effect of discouraging other potential contributors from working on an issue or creating an equivalent pull request.
Net so, wat nie op die tone van hul bydraers wil “stap” nie, is Onderhouders dikwels onseker oor of nie bereid om 'n onvoltooide trekversoek te “oor te neem”, bv. deur eensydig die veranderinge aan te bring wat self vereis word voordat hulle saamsmelt.
Die aanbevelings hieronder is ontwerp om hierdie kwessies aan te spreek en 'n stel “sosiale norme” vir die Carpentries-gemeenskap vas te stel wat moontlik maak dat vordering gemaak kan word op ons bewaarplekke terwyl ons \[kernwaardes] \[waardes] weerspieël - veral dat ons alle bydraes waardeer.

#### Situasie 1: 'n trekversoek bestaan, maar is onvolledig

##### Vir Onderhouders

As 'n trekversoek geopen is, maar nie gereed is om saamgesmelt te word nie, en die oorspronklike bydraer nie gereageer het op 'n boodskap wat dit vir ten minste drie weke merk en 'n opdatering vra nie, en ook nie enige veranderinge aan die tak gestoot het nie, word Onderhouders aangemoedig om enige van die volgende aksies te neem:

1. As slegs geringe veranderinge wag (en u het die vermoë om die tak van die bydraer te wysig), pleeg die veranderinge self toe, \[voeg die persoon wat die PR oopgemaak het as 'n mede-outeur by] \[komite-mede-outeurs] en voeg die trekversoek saam. Let daarop dat, as u veranderinge direk aan die trekversoek op GitHub voorgestel het, **die skrywer van die trekversoek outomaties as 'n mede-outeur** op die verdrag (s) ingesluit sal word wanneer u hierdie veranderinge aanvaar.
2. As groter veranderinge nodig is, \[lewer kommentaar op die trekversoek om ander te nooi] (#inviting-other-contributors-to-complete-an-open-pull-request) om op te pak waar die oorspronklike bydraer ophou het (skakel na \[instruksies vir hoe om die oorspronklike bydraers se tak die doeltreffendste te kopieer en te bou] \[setup-onfinished-tak]). Voeg die etiket `help wanted` by die trekversoek.
3. As u beoordeel dat nog te veel gedoen moet word op die trekkversoek sodat iemand dit kan haal en die taak kan voltooi (of dit het te verouderd geword), sluit die trekversoek toe met ['n opmerking wat die oorspronklike bydraer nooi om weer oop te maak] (#closing-a-stale-pull-request) as hulle daaraan wil aanhou werk. As die probleem wat aangespreek word, voorheen “status: aan die gang” gemerk is, verwyder die etiket en voeg eerder `help wanted` by.

##### Vir bydraers

As 'n trekversoek geopen is, maar nie gereed is om saamgesmelt te word nie, en die oorspronklike bydraer vir ten minste drie weke nie gereageer of enige veranderinge gedruk het nie, word enige gemeenskapslid wat wil bydra tot die voltooiing van die nodige veranderinge aangemoedig om die volgende aksies te neem:

1. Plaas eers na die bestaande trekversoek, met die oorspronklike skrywer en die lesOnderhouers te merk, om almal te laat weet dat u wil help om die trekversoek gereed te maak om saam te voeg. (Onderhouders kan as 'n span gekontak word deur `@lesson -program/lesson-name-maintainers` te merk, bv. `@datacarpentry /R-Ecologie-leson-Maintainers`.) Vra die oorspronklike bydraer of hulle nog aan die trekversoek werk, en of hulle hulp wil hê.
2. As u na 'n paar dae geen antwoord van die oorspronklike bydraer ontvang het nie, moet u hul bewaarplek, insluitend alle takke, of haal hul tak na u plaaslike kloon van die lesbewaarplek en maak addisionele verbintenis aan die tak waaraan hulle gewerk het. (\[Meer gedetailleerde instruksies vir die bou bo-op 'n ander persoon se tak] \[instup-onfinished-tak].) Dit sal verseker dat die werk wat hulle reeds gedoen het, in die geskiedenis van u veranderinge ingesluit word. As u dink dit is gepas, kan u ook \[hulle as mede-outeur byvoeg] \[komite-mede-outeurs] op enige nuwe verbindings wat u maak.
3. Alternatiewelik kan jy ook van nuuts af begin in 'n heeltemal nuwe tak wat uit `main` geskep is. As u kies om dit te doen, maak seker dat u die Onderhouders vertel sodat hulle die oorspronklike trekversoek kan sluit. Oorweeg ook om die skrywer van die oorspronklike (nou geslote) trekversoek as \[mede-outeur] \[komite-mede-outeurs] by te voeg op die verbindings wat u maak, indien die onvoltooide veranderinge wat hulle aangebring het, inspirasie vir u eie verskaf het.

#### Situasie 2: iemand het gesê dat hulle aan 'n kwessie sal werk, maar geen PR verskyn

##### Vir Onderhouders

As die oorspronklike opmerking meer as drie weke gelede gemaak is, en die bydraer nie gereageer het op ['n boodskap wat hulle merk om te vra of hulle nog van plan is om 'n PR voor te berei] (#asking-for-an-update-on-an-issue), word Onderhouders aangemoedig om kommentaar te nooi om ander te werk om aan 'n oplossing te werk, en die etiket \`status: in progress' verwyder as dit voorheen bygevoeg is. Voeg eerder die etiket “help want” by.

##### Vir bydraers

As u agterkom dat 'n ander gemeenskapslid gesê het dat hulle aan 'n probleem wil werk en u nie 'n gepaardgaande terugversoek van hulle kan vind nie, plaas dit op die kwessiedraad en merk daardie gemeenskapslid, om te vra of hulle nog daaraan werk en of hulle enige hulp wil hê. As u binne drie weke geen antwoord ontvang nie, of 'n Onderhouder hulle voorheen vir 'n opdatering gevra het en vir 'n soortgelyke tydperk geen antwoord ontvang het nie, antwoord om almal te laat weet dat u daaraan sal begin werk en 'n trekversoek soos gewoonlik sal voorberei.

#### Boodskapsjablone vir onderhouders

**U hoef nie hierdie sjablone te gebruik nie** maar dit word as voorgestelde taal verskaf om met bydraers na u lesbewaarplek te kommunikeer. Die belangrike dinge wanneer u met bydraers oor onvoltooide bydraes kommunikeer, is:

- Uit dankbaarheid uit vir hul betrokkenheid en bydraes tot dusver.
- Wees duidelik oor die optrede wat hulle en ander moontlike bydraers moet neem.
- Nooi hulle uit om te reageer.

##### Nooi ander bydraers uit om 'n oop trekversoek te voltooi

Vervang `@USERNAME` met die GitHub-handvatsel van die bydraer wat oorspronklik die trekversoek oopgemaak het.

```markdown
Dit sal goed wees om hierdie veranderinge binnekort by die les ingesluit te hê. Dankie @USERNAME vir jou bydraes tot dusver. 
Aangesien vordering 'n rukkie gestaak is, nooi ek enige ander gemeenskapslede wat dit lees, uit om die taak aan te neem om die oorblywende veranderinge aan te bring wat nodig is om dit saamgesmelt te word. 
As u dit doen, moet u asseblief [bou bo-op die werk wat reeds deur @USERNAME gedoen is] (https://docs.carpentries.org/resources/curriculum/fetch-existing-branch.html) sodat hul bydraes in die verpligingsgeskiedenis ingesluit word. 
Plaas gerus hier as u enige vrae het oor wat nog gedoen moet word voordat die tak saamgesmelt kan word.

@USERNAME as jy wil aanhou werk aan die trekversoek, plaas asseblief hier om ons te laat weet en vertel ons of daar iets is wat ons kan doen om te help.
```

##### Sluit 'n verouderde trekversoek

Vervang `@USERNAME` met die GitHub-handvatsel van die bydraer wat oorspronklik die trekversoek oopgemaak het.

```markdown
Dankie @USERNAME vir jou bydraes tot dusver. 
Aangesien vordering vir 'n rukkie gestaak is en dit vir 'n ander gemeenskapslid moeilik kan wees om die werk wat reeds hier gedoen is, sal ek hierdie trekversoek nou sluit. 

@USERNAME As jy wil voortgaan om aan hierdie veranderinge te werk, maak asseblief die trekversoek weer oop en ek sal jou graag help.
```

##### Vra vir 'n opdatering oor 'n probleem

Vervang `@USERNAME` met die GitHub-handvatsel van die bydraer wat oorspronklik die trekversoek oopgemaak het.

```markdown
@USERNAME dit is al 'n rukkie sedert ons van u gehoor het en ek het nog nie 'n trekversoek gesien om hierdie probleem aan te spreek nie.
Dit sal goed wees om hierdie probleem opgelos te laat en ek weet dat dit dikwels 'n geruime tyd neem om veranderinge aan 'n les aan te bring. 
Kan jy 'n opdatering verskaf oor jou vordering? Is daar iets wat die Onderhouders kan doen om jou te help met jou trekversoek?

As jou omstandighede of kapasiteit verander het, en jy nie meer kan help met hierdie probleem nie, is dit ook goed. Laat ons asseblief hier weet, sodat ons u kan help en/of ander lede van die gemeenskap kan begin werk aan die kwessie.
```

[commit-coauthors]: https://github.blog/2018-01-29-commit-together-with-co-authors/
[setup-unfinished-branch]: <.. /hulpbronne/kurrikulum/haal-bestaande-branch.md>
[values]: https://carpentries.org/about-us/#our-values


