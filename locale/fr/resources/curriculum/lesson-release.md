# Publier une leçon

**Notez que les responsables des cours de menuiserie de données, de menuiserie de bibliothèque et de menuiserie logicielle ne devraient pas publier de leçons pour l'instant.**
L'équipe chargée du programme coordonnera ce processus dans les mois à venir.

La publication régulière de votre leçon vous donne, à vous et à vos contributeurs, l'occasion de célébrer les améliorations qui ont été apportées et de leur permettre d'obtenir plus facilement des crédits et une reconnaissance pour le travail qu'ils ont accompli.
Il est particulièrement important de publier la leçon lorsqu'elle atteint des étapes clés de son développement, par exemple avant [des ateliers pilotes bêta] (lesson-pilots.md) ou lorsqu'elle atteint [un état stable] (./lesson-life-cycle.md).

Si vous [publiez la leçon sur Zenodo] (#publishing-the-lesson-on-zenodo) lorsque vous la publiez, vous recevrez un identifiant d'objet numérique que vous et d'autres personnes pourrez utiliser pour faire référence à la leçon et/ou à une version particulière.
La publication de la leçon permet à d'autres personnes de la retrouver plus facilement et, si vous incluez votre identifiant [ORCID iD] (https://info.orcid.org/what-is-orcid/) dans les informations relatives à ses auteurs, vous pouvez répertorier le projet sur votre profil public.

## Préparation d'une sortie

### Mise à jour des informations de citation

Les référentiels de leçons peuvent contenir des informations de citation au format [Citation File Format] (https://citation-file-format.github.io/).
Le programme de formation à l'élaboration de leçons en collaboration inclut [une discussion sur les raisons pour lesquelles vous devriez inclure ce fichier dans votre référentiel de leçons] (https://carpentries.github.io/lesson-development-training/collaborating-newcomers.html#helping-people-cite-your-lesson).
La documentation de Carpentries Workbench décrit plus en détail [comment le fichier peut être inclus dans le référentiel] (https://carpentries.github.io/sandpaper-docs/editing.html#making-your-lesson-citable) et donne un exemple.

Nous vous recommandons de mettre à jour les informations relatives aux citations au fur et à mesure que vous progressez dans le développement et la mise à jour des leçons.
À tout le moins, vous devez vous assurer que les informations de votre `Citation.cff` sont à jour avant de publier une nouvelle version de votre leçon, car cela simplifiera le processus de publication sur Zenodo.

## Publier la leçon sur Zenodo

- Tout d'abord, créez un compte [Zenodo] (https://zenodo.org/) si vous n'en avez pas déjà un, lié à vos informations d'identification GitHub.
- Connectez-vous à Zenodo et sélectionnez « GitHub » dans le menu déroulant en haut à droite.
- Sur cette page, recherchez le nom de votre référentiel de leçons dans la liste et activez le commutateur « On » pour activer l'intégration Zenodo/GitHub.
- [Publiez votre leçon] (https://docs.github.com/en/repositories/releasing-projects-on-github/managing-releases-in-a-repository#creating-a-release) depuis son référentiel GitHub. Cela créera un enregistrement Zenodo à partir de cette version. Zenodo mettra à jour cet enregistrement avec une nouvelle version chaque fois que vous créerez une nouvelle version à partir de votre référentiel de leçons.
- Modifiez l'entrée Zenodo pour ajuster tout ce qui ne va pas.
  Par exemple, la présence d'un fichier Citation.cff dans votre dépôt fera penser à Zenodo qu'il s'agit d'un enregistrement décrivant un logiciel.
  Vous pouvez corriger cela en « Leçon » dans le champ _Resource Type_.
- Ajoutez le DOI de votre enregistrement aux fichiers « README.md » et « Citation.cff » de votre référentiel de leçons.
  L'enregistrement créé à partir de votre version inclura deux DOI : un pour la version spécifique publiée cette fois, et un second DOI de « niveau supérieur » qui correspondra toujours à la dernière version de la leçon publiée.
  Nous vous recommandons d'ajouter le DOI de « niveau supérieur » aux fichiers de votre référentiel de leçons. Zenodo vous donne un code Markdown pour afficher une icône de « badge », par exemple ! [DOI] (https://zenodo.org/badge/DOI/10.5281/zenodo.8415001.svg) dans le README de votre dépôt.
  Recherchez le champ DOI dans la case _Details_ à droite de la page d'enregistrement pour trouver votre badge.

