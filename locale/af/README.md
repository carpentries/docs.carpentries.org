# Die Carpentries Handboek

Dit is die repo wat [The Carpentries Handbook] (https://docs.carpentries.org) bou.

## webwerforganisasie

Hierdie handboek het drie hoofafdelings:

- **Handboek**.  Dit bevat handboeke vir elke gemeenskapsrol (gemeenskapsessie-gasheer, instrukteur, ens.).  Elke gemeenskapsrol het dieselfde volgende afdelings om te verseker dat gebruikers 'n inhoudende ervaring het terwyl hulle elke rol ondersoek.
  - Rolle en verantwoordelikhe
  - Onboord
  - Afboording
  - Kommunikasie- en samewerkings
  - Stap vir stap gidse
  - Hulpbronne
  - FAQ
- **Hulpbronne**.  Dit is 'n lys van algemene hulpbronne wat beskikbaar is vir die Carpentries-gemeenskap (Stylgids, Kommunikasiebronne, ens.).
- **Beleids**.  Dit is 'n lys van alle Carpentries -beleide (gedragskode, privaatheid, ens.)

## Lêerstruktuur

- `/bou/` Word gebruik om plaaslike webwerf te bou. In `.gitignore` sal dit dus nie in die repo verskyn nie.  Moenie hierdie lêers wysig nie.
- `/bron/` Bevat al die lêers wat nodig is om die webwerf te bou.  Sluit in:
  - css-lêers en bladsysjablone wat style en sjablone in die tema oorheers
  - vouers vir handboeke, hulpbronne en beleide, met `md` lêers met inhoud vir elke bladsy.
  - `/_includes/` - teksblokke en ander inhoud wat op ander bladsye ingesluit moet word
  - `/_templates/` - sjablone vir gespesialiseerde inhoud soos die inhoudsopgawe in die kantbalk
  - `/_static/` - bevat persoonlike css-style
  - `conf.py` - webwerfinstellings
  - `index.rst` - stel struktuur vir tuisblad
- `.gitignore` Standaard gitignore lêer
- `Makefile` - sluit pasgemaakte Make-opdragte in en erf algemene Sphinx Make-opdragte.

## Redigeer inhoud

Inhoud is georganiseer in die “bron” -gids.  Wysigings aan die inhoud moet aan hierdie lêers gemaak word.  Moenie lêers in die `build` -lêergids wysig nie.

## Redigeerstyle

Die meeste stilering kom van die `pydata_sphinx_theme` sjabloon.  Pasgemaakte style word geïmplementeer in `/source/_static/css`.  Dit sluit die lettertiplêers vir die Mulish Google-lettertipe en 'n pasgemaakte css-lêer in.

## Redigeer sjablone en uitlegte

Die meeste sjablone en uitlegte kom van die `pydata_sphinx_theme` sjabloon.  Pasgemaakte bladsysjablone word geïmplementeer in `/bronce/_templates/`.  Die standaardtema bevat byvoorbeeld Python-funksies om sjablone vir die inhoudsopgawe in die kantbalk en boonste navigasiebalk te bou. In plaas daarvan gebruik ons pasgemaakte en hard gekodeerde sjablone.  Dit word dan genoem in `html_theme_options` in `conf.py`.

## Die bou van die handboek plaaslik

Die handboek is gebou met behulp van Sphinx en die `pydata_sphinx_theme`.

- `maak skoon` Verwyder alle lêers in die `build` gids
- `make html` Bou die webwerf en publiseer html-inhoud in die bougids. Begin 'n Python-bediener met `python -m http.server -d build/html/` om die webwerf te voorsien. Die webwerf sal met elke verandering weer gebou moet word.

Alternatiewelik, gebruik `sphinx-autobuild` om die webwerf te herbou en die blaaier weer te laai wanneer veranderinge aangebring word met `sphinx-autobuild source/ build/html/`

## Veranderinge aan `conf.py`

Nadat die tema ingestel is, was die bykomende volgende veranderinge nodig om `conf.py`.  Let daarop dat hierdie lys nie veranderinge bevat wat slegs The Carpentries identiteit weerspieël nie (instelling van die naam, sosiale media handvatsels, ens.).  Die lys bevat veranderinge wat die funksionaliteit van die webwerf beïnvloed.

- Om die sjabloon die markdownlêers behoorlik te laat weergee, voeg `.md` by die `source_suffix` -lys en voeg `myst_parser` by die \`uitbreidings' lys
- Om 'n custon-stylblad te gebruik, stel `html_static_path = ['_static'] `en `html_css_files = ['css/custom.css']`
- Voeg navbalk- en sykantinstellings by `html_context`
- Om kopskrifte as ankerskakels te gebruik, voeg `myst_heading_anchors = 6` by
- Om waarskuwings oor duplikaatkopskrifte oor dokumente te onderdruk, voeg `suppress_warning = ['autosectionlabel.*'] `by

## Nuttige skakels

- [Pydata Sfinx Tema] (https://pydata-sphinx-theme.readthedocs.io/en/stable/index.html)
- [Algemene Sfinks-dokumentasie] (https://www.sphinx-doc.org/en/master/usage/configuration.html)
