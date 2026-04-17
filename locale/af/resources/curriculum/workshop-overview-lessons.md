# Kurrikulumoorsigbladsye

Die Carpentries Workbench is standaard ontwerp om [leswebwerwe bestaande uit verskeie episode bladsye] (./curriculum-structure.md) te bou, wat die tipiese struktuur van ons lesse weerspieël.
Dit is egter soms nuttig om 'n enkelbladsy-leswebwerf te kan verskaf, tipies as 'n oorsig of 'landingsblad' vir 'n versameling lesse wat bymekaar behoort ([ons noem dit 'n _kurrikulum_] (./curriculum-structure.md)).

In die Workbench word dit ondersteun met die opsionele `oorsig'-parameter in die globale konfigurasielêer (`config.yaml`).
Die byvoeging van `oorsig: true`as 'n nuwe reël na`config.yaml`verhoed dat die infrastruktuur 'n fout veroorsaak as geen lêers in die`episodes`-lêers teenwoordig is nie. Die voorblad van die oorsigwebwerf is gebou uit die`index.md`en`leerners/setup.md\` soos gewoonlik.

## Wat moet 'n oorsigbladsy bevat?

Lesontwikkelaars kan kies om hierdie bladsye te bevul soos hulle wil.
Hier is 'n paar aanbevelings vir wat om in te sluit:

- 'N Kort beskrywing van die kurrikulum as geheel, insluitend die teikengehoor en die belangrikste leeruitkomste.
- 'N Lys van voorvereiste kennis vir die kurrikulum. (Dit kan geformateer word as 'n omheinde div met die `prereq` klas.)
- 'N Tabel beskryf die lesse wat in die kurrikulum ingesluit is, en die aanbevole volgorde waarin hulle geleer moet word.
  - As verskeie moontlike paaie deur u kurrikulum bestaan, moet dit beskryf word as individuele tabelle of in 'n inleidende teks voordat die tabel van alle lesse vertoon word. As daar baie paaie deur u lesse bestaan, beskryf dit op 'n aparte bladsy wat uit 'n bronlêer in die `leerders/` -lêergids gebou is en skakel daarna vanaf `index.md`.
- Opstelinstruksies soos vir sagteware-installasie en data-aflaai moet in `leers/setup.md` beskryf word.
  Soos met 'n les in die standaardkonfigurasie, sal die inhoud van hierdie bladsy by die landing bladsy van die webwerf aangeheg word.
- As u lesse 'n algemene voorbeelddatastel deel, wil u dit dalk op 'n toegewyde bladsy op hierdie oorsigwebwerf beskryf.
  Hierdie bladsy kan byvoorbeeld 'n _data-woordeboek_ insluit wat die kenmerke van die datastel beskryf, 'n kort beskrywing van die oorsprong daarvan, 'n skakel na die rou data en 'n skakel na verdere inligting (bv. 'n publikasie met die oorspronklike data).
  - Sien die [_Workshopdata_ -bladsy van die Data Masinery Ecology Curriculum Overview] (https://datacarpentry.org/ecology-workshop/data.html) vir 'n voorbeeld.

Al die items wat hierbo beskryf word, moet ingesluit word in die oorsigwebwerf van 'n amptelike Carpentries-kurrikulum.

## Sjabloon Markdown vir kurrikulumoorsigtabel

Maak 'n afskrif van hierdie sjabloon om jou te help om 'n Markdown-tabel te bou wat die lesse in jou kurrikulum beskryf.

```markdown
| **Les** | **Oorsig** |
|: -------------------------------------------- | -------------------------------------------------------------------------- |
| [Titel van die eerste les] (URL-of-lesson-site) | 'n Kort beskrywing wat die eerste les leer |
| [Titel van die tweede les] (URL-of-lesson-site) | 'n Kort beskrywing wat die tweede les leer | 
|... | Hou voeg lyne in hierdie formaat by totdat u al u lesse gelys het
```
