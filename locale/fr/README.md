# Le manuel de menuiserie

C'est le repo qui construit [The Carpentries Handbook] (https://docs.carpentries.org).

## Organisation du site

Ce manuel comprend trois sections principales :

- **Manuels**.  Il contient des manuels pour chaque rôle dans la communauté (animateur de session communautaire, instructeur, etc.).  Chaque rôle dans la communauté comporte les sections suivantes, afin de garantir aux utilisateurs une expérience cohérente lorsqu'ils explorent chaque rôle.
  - Rôles et responsabilités
  - Intégration
  - Débarquement
  - Espaces de communication et de collaboration
  - Guides étape par étape
  - Ressources
  - FAQ
- **Ressources**.  Voici une liste des ressources générales disponibles pour la communauté The Carpentries (guide de style, ressources de communication, etc.).
- **Politiques**.  Voici une liste de toutes les politiques de Menuiseries (code de conduite, confidentialité, etc.)

## Structure des fichiers

- `/build/` Utilisé pour créer un site Web local. Dans `.gitignore`, cela n'apparaîtra pas dans le dépôt.  Ne modifiez pas ces fichiers.
- `/source/` Contient tous les fichiers nécessaires à la création du site.  Comprend :
  - fichiers CSS et modèles de page qui remplacent les styles et les modèles du thème
  - dossiers pour les manuels, les ressources et les politiques, avec des fichiers « md » avec du contenu pour chaque page.
  - `/_includes/` - blocs de texte et autres contenus à inclure dans d'autres pages
  - `/_templates/` - modèles pour du contenu spécialisé tel que la table des matières dans la barre latérale
  - `/_static/` - contient des styles CSS personnalisés
  - `conf.py` - paramètres du site
  - `index.rst` - définit la structure de la page d'accueil
- `.gitignore` Fichier gitignore standard
- `Makefile` - inclut des commandes Make personnalisées et hérite des commandes générales de Sphinx Make.

## Modifier le contenu

Le contenu est organisé dans le répertoire « source ».  Le contenu de ces fichiers doit être modifié.  Ne modifiez pas les fichiers du dossier `build`.

## Styles d'édition

La plupart des styles proviennent du modèle pydata_sphinx_theme.  Les styles personnalisés sont implémentés dans `/source/_static/css`.  Cela inclut les fichiers de police pour la police Mulish Google et un fichier CSS personnalisé.

## Modification de modèles et de mises en page

La plupart des modèles et des mises en page proviennent du modèle pydata_sphinx_theme.  Les modèles de page personnalisés sont implémentés dans `/source/_templates/`.  Par exemple, le thème standard inclut des fonctions Python permettant de créer des modèles pour la table des matières dans la barre latérale et la barre de navigation supérieure. Nous utilisons plutôt des modèles personnalisés et codés en dur.  Ils sont ensuite appelés dans html_theme_options dans conf.py.

## Création du manuel localement

Le manuel est construit à l'aide de Sphinx et du pydata_sphinx_theme.

- `make clean` Supprime tous les fichiers du répertoire `build`
- `make html` Construit le site et publie le contenu HTML dans le répertoire de construction. Exécutez un serveur Python avec « python -m http.server -d build/html/ » pour prévisualiser le site. Le site devra être reconstruit à chaque modification.

Vous pouvez également utiliser sphinx-autobuild pour reconstruire le site et recharger le navigateur chaque fois que des modifications sont apportées avec sphinx-autobuild source/ build/html/

## Modifications apportées à `conf.py`

Après avoir défini le thème, les modifications supplémentaires suivantes ont été nécessaires pour `conf.py`.  Notez que cette liste n'inclut pas les modifications qui reflètent uniquement l'identité de The Carpentries (définition du nom, pseudonymes sur les réseaux sociaux, etc.).  La liste inclut les modifications qui affectent les fonctionnalités du site.

- Pour que le modèle affiche correctement les fichiers de démarquage, ajoutez `.md` à la liste `source_suffix` et ajoutez `myst_parser` à la liste `extensions`
- Pour utiliser une feuille de style personnalisée, définissez `html_static_path = ['_static'] `et `html_css_files = ['css/custom.css']`
- Ajoutez les paramètres de la barre de navigation et de la barre latérale à `html_context`
- Pour utiliser les en-têtes comme liens d'ancrage, ajoutez `myst_heading_anchors = 6`
- Pour supprimer les avertissements concernant les doublons d'en-têtes dans les documents, ajoutez `suppress_warnings = ['autosectionlabel.*'] `

## Liens utiles

- [Thème Pydata Sphinx] (https://pydata-sphinx-theme.readthedocs.io/en/stable/index.html)
- [Documentation générale sur le Sphinx] (https://www.sphinx-doc.org/en/master/usage/configuration.html)
