# Die bekendstelling van 'n les

**Let daarop dat onderhouders van datammerwerk-, biblioteektimmerwerk- en sagtewarestuurlesse vir nou nie lesvrystellings moet maak nie.**
Die kurrikulumspan sal hierdie proses in die komende maande koördineer.

Om gereelde vrystellings van jou les te maak, gee jou en jou bydraers die geleentheid om die verbeterings wat aangebring is te vier, en dit vir hulle makliker maak om krediet en erkenning te ontvang vir die werk wat hulle ingebring het.
Dit is veral belangrik om die les vry te stel wanneer dit belangrike mylpale in sy ontwikkeling bereik, bv. voor [beta-piloetwerkswinkels] (lesson-pilots.md) of wanneer dit ['n stabiele toestand] bereik (./lesson-life-cycle.md).

As u [die les oor Zenodo publiseer] (#publishing-the-lesson-on-zenodo) wanneer u dit vrystel, sal u 'n digitale voorwerp-identifiseerder ontvang wat u en ander kan gebruik om na die les en/of 'n spesifieke weergawe te verwys.
As u die les publiseer, maak dit meer vindbaar deur ander mense, en - as u u [ORCID iD] (https://info.orcid.org/what-is-orcid/) -identifiseerder in die inligting oor die skrywers daarvan insluit - help u om die projek op u openbare profiel te lys.

## Voorbereiding vir 'n vrylating

### Opdatering van aanhalingsinligting

Lesbewaarplekke kan aanhalingsinligting bevat in [Citation File Format] (https://citation-file-format.github.io/).
Die kurrikulum vir samewerkende lesontwikkelingsopleiding bevat ['n paar bespreking waarom u hierdie lêer in u lesbewaarplek moet insluit] (https://carpentries.github.io/lesson-development-training/collaborating-newcomers.html#helping-people-cite-your-lesson).
Die Carpentries Workbench -dokumentasie beskryf in meer besonderhede [hoe die lêer in die bewaarplek ingesluit kan word] (https://carpentries.github.io/sandpaper-docs/editing.html#making-your-lesson-citable) en gee 'n voorbeeld.

Ons beveel aan dat u aanhalingsinligting bygewerk hou terwyl u vorder met lesontwikkeling en -instandhouding.
Ten minste moet u verseker dat die inligting in u `Citation.cff` aktueel is voordat u 'n nuwe weergawe van u les vrystel, want dit sal die proses om dit aan Zenodo vrygestel te stel, vereenvoudig.

## Publiseer die les oor Zenodo

- Skep eers 'n [Zenodo] (https://zenodo.org/) -rekening as u nie reeds een het nie, gekoppel aan u GitHub-bewysings.
- Meld by Zenodo aan en kies 'GitHub' in die keuselys regs bo.
- Vind op daardie bladsy die naam van u lesbewaarplek in die lys en draai die skakelaar 'Aan' om die Zenodo/GitHub-integrasie te aktiveer.
- [Maak 'n vrystelling van jou les] (https://docs.github.com/en/repositories/releasing-projects-on-github/managing-releases-in-a-repository#creating-a-release) uit sy GitHub-bewaarplek. Dit sal 'n Zenodo-rekord uit die vrystelling skep. Zenodo sal hierdie rekord opdateer met 'n nuwe weergawe elke keer as u nog 'n vrystelling uit u lesbewaarplek maak.
- Wysig die Zenodo-inskrywing om enigiets aan te pas wat nie reg is nie.
  Byvoorbeeld, die teenwoordigheid van 'n `Citation.cff` -lêer in jou bewaarplek sal Zenodo laat dink dit is 'n rekord wat sagteware beskryf.
  U kan dit regstel na 'Les' in die _Resource Type_ veld.
- Voeg die DOI vir jou rekord by die `README.md`- en `Citation.cff` -lêers in jou lesbewaarplek.
  Die rekord wat uit u vrystelling geskep is, sal twee DOI's insluit: een vir die spesifieke weergawe wat hierdie keer vrygestel is, en 'n tweede 'top-vlak' DOI wat altyd sal oplos op die nuutste weergawe van die les wat vrygestel is.
  Ons beveel aan dat u die 'top-vlak' DOI by die lêers in u lesbewaarplek voeg. Zenodo gee jou Markdown-kode om 'n 'kenteken' -ikoon te vertoon bv.! [DOI] (https://zenodo.org/badge/DOI/10.5281/zenodo.8415001.svg) op jou bewaarplek README.
  Soek die DOI-veld in die _Details_ blokkie regs van die rekordbladsy om u kenteken te vind.

