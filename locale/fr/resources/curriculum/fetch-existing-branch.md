# S'appuyer sur la succursale existante de quelqu'un d'autre

Parfois, il se peut que vous souhaitiez ou deviez vous appuyer sur les modifications qu'une autre personne a déjà apportées à une branche d'un référentiel de leçons, par exemple [si elle n'est plus en mesure de terminer le travail et que vous souhaitez l'aider à terminer sa pull request] (/handbooks/maintainers.md#situation-1-a-pull-request-exists-but-is-incomplete).
Cette page décrit deux manières de vous configurer pour tirer parti des modifications déjà apportées.
Les instructions supposent une certaine familiarité avec le contrôle de version, Git et GitHub.

## 1. Forker leur référentiel et leur branche

### Trouvez le fork original du contributeur

À partir de la pull request ouverte sur laquelle vous souhaitez continuer à travailler, faites défiler l'onglet _Conversation_ vers le haut.
Sous le titre de la pull request, vous trouverez un résumé des branches qui seraient combinées si la pull request était fusionnée : généralement, l'organisation du programme de cours et « main » sur la gauche, et le nom d'utilisateur du contributeur d'origine et le nom de la branche qu'il a choisi sur la droite (la « branche de fonctionnalité »).

! [Informations sur la succursale pour une pull request sur GitHub. Le nom de la branche par défaut du référentiel officiel, `datacarpentry:main`, et de la branche fonctionnelle du contributeur, `example-user:example-branch`, sont affichés.] (./img/branch-info-pr.png)

En cliquant sur le nom de la branche de fonctionnalités du contributeur, vous serez redirigé vers cette branche sur son fork du référentiel de leçons.

### Fabriquez votre propre fourchette à partir de la leur

À partir de cette page, vous pouvez créer votre propre fork de leur dépôt à l'aide du bouton « Fork » en haut à droite de la page.
Cela ouvrira un court formulaire, dans lequel vous pourrez définir un nom et une description pour le nouveau fork que vous allez créer.
La chose importante à faire ici est de \*\*décocher la case « Copier la branche principale uniquement » \*\* afin d'obtenir également une copie de la branche de fonctionnalité sur laquelle ils travaillaient pour la pull request.

! [Le formulaire présenté lors du fork d'un référentiel existant sur GitHub, avec la case « Copier la branche principale uniquement » décochée.] (./img/new-fork-all-branches.png)

### Modifier la leçon sur GitHub

Une fois votre fork créé, utilisez la liste déroulante en haut à gauche de la page d'accueil du référentiel pour choisir la branche sur laquelle le contributeur d'origine travaillait.
Une fois cette branche sélectionnée, vous pouvez commencer à modifier les fichiers sur GitHub en prenant soin de valider vos modifications dans cette même branche.
Vous pouvez également [ouvrir l'IDE github.dev dans votre navigateur] (https://docs.github.com/en/codespaces/the-githubdev-web-based-editor#opening-the-githubdev-editor), sélectionner la branche et continuer à la modifier et à la commiter.

### Modifier la leçon localement

Suivez ces étapes une fois que votre fork a été créé.

1. Clonez-le sur votre système local.
2. Dans le shell, accédez à votre clone local du projet, par exemple « cd ~/Documents/DataCarpEntry/R-Ecology-Lesson ».
3. Récupérez la branche sur laquelle le contributeur d'origine travaillait (`git fetch origin <their-branch-name>`, par exemple `git fetch origin 123-better-captions`).
4. Passez dessus (`git switch <their-branch-name>`, par exemple `git switch 123-better-captions`).

Une fois que vous avez travaillé sur cette branche, vous pouvez modifier la leçon et valider vos modifications comme d'habitude.
Lorsque vous êtes prêt, ajoutez votre propre fork du référentiel des leçons en tant que télécommande (`git remote add <remote-name> <address-of-forked-repository-you-just-copied>`, par exemple `git remote add myfork git@github.com:myusername/image-processing.git`), poussez les commits que vous avez effectués et ouvrez une pull request vers le référentiel officiel.

## 2. Ajouter leur fork en tant que référentiel distant

Si vous possédez déjà un clone local du référentiel de leçons, vous pouvez ajouter le fork de la leçon créé par le contributeur d'origine en tant que référentiel distant pour le projet et récupérer la branche sur laquelle il travaillait à partir de là.

1. Suivez les étapes décrites dans [_Trouvez le fork du contributeur d'origine_] (#1-fork-their-repository-and-branch) ci-dessus.
2. Cliquez sur le bouton _Code_ et copiez l'adresse de ce référentiel dans votre presse-papiers.
3. Dans le shell, accédez à votre clone local du projet, par exemple « cd ~/Documents/DataCarpEntry/R-Ecology-Lesson ».
4. Ajoutez le fork du contributeur d'origine en tant que nouveau dépôt distant pour ce clone : `git remote add <remote-name> <address-of-forked-repository-you-just-copied>`,
   par exemple `git remote add toby git@github.com:tobyhodges/image-processing.git`.
5. Récupérez la branche sur laquelle ils travaillaient depuis leur fork, par exemple `git fetch toby 123-better-captions`.
6. Passez à cette branche, par exemple `git switch 123-better-captions`.

Une fois que vous avez travaillé sur cette branche, vous pouvez modifier la leçon et valider vos modifications comme d'habitude, puis les envoyer vers votre fork et ouvrir une pull request lorsque vous êtes prêt.

## Ouvrir une pull request avec vos mises à jour

Lorsque vous êtes prêt à ouvrir une nouvelle demande d'extraction qui inclura vos modifications, assurez-vous de le faire dans le référentiel approprié (généralement un référentiel appartenant à l'une des organisations officielles de The Carpentries, par exemple « datacarpentry ») : GitHub peut d'abord essayer de vous aider à ouvrir une pull request vers le fork du contributeur d'origine au lieu du référentiel central de Carpentries.

Lorsque vous ouvrez votre pull request, dites aux responsables que vous avez construit sur la base du travail précédent de l'autre contributeur. Marquez ce contributeur d'origine et faites référence à sa pull request par son numéro, par exemple `Cette pull request s'appuie sur et remplace #37 par @USERNAME pour fermer le problème #34 par [une description des modifications apportées à votre pull request...] `.
Cela aidera les responsables de la leçon à comprendre qu'ils peuvent fermer l'autre pull request et à comprendre la relation entre les deux ensembles de modifications.
