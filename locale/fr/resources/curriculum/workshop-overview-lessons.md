# Pages de présentation du programme

Par défaut, The Carpentries Workbench est conçu pour créer [des sites Web de leçons composés de plusieurs pages d'épisodes] (./curriculum-structure.md), reflétant la structure typique de nos leçons.
Cependant, il est parfois utile de pouvoir proposer un site de « leçons » d'une seule page, généralement sous forme d'aperçu ou de « page de destination » pour un ensemble de leçons qui vont ensemble ([nous appelons cela un _curriculum_] (./curriculum-structure.md)).

Dans le Workbench, cela est pris en charge par le paramètre optionnel `overview` dans le fichier de configuration global (`config.yaml`).
L'ajout de `overview : true `comme nouvelle ligne à `config.yaml` empêche l'infrastructure de générer une erreur si aucun fichier n'est présent dans le dossier `episodes`. La page d'accueil du site de présentation est construite à partir du `index.md` et du `learners/setup.md` comme d'habitude.

## Que doit contenir une page de présentation ?

Les développeurs de leçons peuvent choisir de remplir ces pages comme bon leur semble.
Voici quelques recommandations sur ce qu'il faut inclure :

- Brève description du programme dans son ensemble, y compris son public cible et ses principaux résultats d'apprentissage.
- Une liste des connaissances préalables au programme. (Cela peut être formaté comme un div clôturé avec la classe `prereq`.)
- Un tableau décrivant les leçons incluses dans le programme et l'ordre recommandé dans lequel elles devraient être enseignées.
  - S'il existe plusieurs parcours possibles dans votre programme, ceux-ci doivent être décrits sous forme de tableaux individuels ou dans un texte d'introduction avant que le tableau de toutes les leçons ne soit affiché. S'il existe de nombreux parcours dans vos leçons, décrivez-les sur une page séparée créée à partir d'un fichier source dans le dossier « learners/ » et créez un lien vers celui-ci depuis index.md.
- Les instructions de configuration, telles que l'installation du logiciel et le téléchargement des données, doivent être décrites dans learners/setup.md.
  Comme pour une leçon de configuration par défaut, le contenu de cette page sera ajouté à la page d'accueil du site.
- Si vos leçons partagent un exemple de jeu de données commun, vous souhaiterez peut-être le décrire sur une page dédiée de ce site de présentation.
  Par exemple, cette page peut inclure un _dictionnaire de données_ décrivant les caractéristiques de l'ensemble de données, une brève description de ses origines, un lien vers les données brutes et un lien vers des informations supplémentaires (par exemple une publication contenant les données d'origine).
  - Consultez la page [_Workshop Data_ de l'aperçu du programme d'écologie de la menuiserie des données] (https://datacarpentry.org/ecology-workshop/data.html) pour un exemple.

Tous les éléments décrits ci-dessus doivent être inclus dans le site de présentation d'un programme officiel de menuiserie.

## Modèle Markdown pour le tableau récapitulatif des programmes

Faites une copie de ce modèle pour vous aider à créer un tableau Markdown décrivant les leçons de votre programme.

```markdown
| **Leçon** | **Aperçu** |
| : ------------------------------------------------------------ | -------------------------------------------------------------------------- |
| [Titre de la première leçon] (URL-of-lesson-site) | Une brève description de ce que la première leçon enseigne |
| [Titre de la deuxième leçon] (URL-of-lesson-site) | Une brève description de ce que la deuxième leçon enseigne | 
|... | Keep ajouter des lignes dans ce format jusqu'à ce que vous ayez listé toutes vos leçons |
```
