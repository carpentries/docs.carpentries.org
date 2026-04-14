# Manuel pour les développeurs de leçons

## À propos de ce manuel

Le manuel des développeurs de leçons est conçu pour aider les membres de la communauté The
Carpentries qui travaillent en tant que développeurs de leçons. Il est géré par l'équipe du programme The Carpentries.  Si vous pensez que quelque chose doit être ajouté ou mis à jour ici, ou si vous souhaitez faire part de vos commentaires sur le contenu, veuillez envoyer un e-mail à {{'[Curriculum Team] (mailto:{}) '.format (curriculum_email)}} ou ouvrez un numéro sur le {{' [référentiel source de ce manuel] ({}) '.format (gh_repo)}}. Si vous ne connaissez aucun des termes utilisés dans ce manuel, veuillez consulter notre {{'[Glossaire des termes] ({}) '.format (glossaire)}}.

## Rôles et responsabilités

Au-delà de s'assurer que la leçon reste conforme aux exigences
pour être incluse dans [The Carpentries
Incubator] (https://github.com/carpentries-incubator/proposals/blob/main/README.md#what-are-the-requirements-for-being-included-in-the-carpentries-incubator),
, aucune responsabilité officielle n'est associée à l'élaboration d'une leçon
dans ce domaine : les projets de cours de l'incubateur sont des efforts communautaires et
appartiennent aux développeurs individuels qui y contribuent. Ces développeurs
peuvent choisir de les gérer et de leur consacrer du temps en fonction de
en fonction de leurs préférences et de leurs disponibilités.

Pour garantir la santé et la durabilité de leur projet de leçon
, The Carpentries recommande aux développeurs de leçons de confier à
la responsabilité des tâches suivantes :

- Gérer la conception et le développement de la leçon.
- Lire, répondre et (si nécessaire) gérer les problèmes
  signalés par les membres de la communauté.
- Accueillir et examiner les pull requests et autres contributions faites par les membres de la communauté
  .
- Communiquer avec la communauté au sujet du développement en cours de la leçon
  .
- Recruter des instructeurs pour tester la leçon en version bêta, soutenir les préparatifs
  pour les ateliers pilotes et intégrer les commentaires de
  à ces ateliers.
- Soumettre la leçon pour évaluation ouverte par les pairs et acceptation à [The
  Carpentries Lab] (https://carpentries-lab.org).

## Intégration

Les développeurs de leçons peuvent commencer une nouvelle leçon à tout moment en ouvrant un nouveau numéro
sur [le référentiel The Carpentries Incubator Proposals
] (https://github.com/carpentries-incubator/proposals/issues/new?assignees=&labels=&template=issue_proposal.md).
Le modèle de problème comprend plusieurs questions auxquelles il convient de répondre
pour aider l'équipe chargée du programme à configurer correctement le référentiel des leçons dans
the Incubator.

Les membres de la communauté qui ont une idée de nouvelle leçon peuvent également s'inscrire pour participer à la formation de développement de leçons collaboratives
, qui sera organisée périodiquement à
à partir de 2023.

## Débarquement

Il n'existe pas de processus d'offboarding officiel pour les développeurs de leçons travaillant sur des projets
dans The Carpentries Incubator.

Pour garantir la santé et la durabilité du projet, The
Carpentries recommande aux développeurs de leçons de prendre les mesures suivantes
lorsqu'ils quittent une leçon :

- Communiquez la décision aux autres développeurs de la leçon, afin qu'ils puissent redistribuer les tâches et planifier le projet en conséquence.
- Réattribuez tous les problèmes qui leur sont assignés à un autre membre de l'équipe de développement des leçons
  .
- Supprimez leur nom du fichier README de la leçon et de tout autre endroit où les auteurs
  de la leçon sont répertoriés.
- Demandez au propriétaire du projet (un développeur disposant d'un accès administrateur au référentiel
  ) de révoquer les privilèges du développeur sortant sur le référentiel de leçons
  .
- Si le seul développeur restant de la leçon quitte le projet,
  ajoute une notice en haut du référentiel README et à la première page
  de la leçon (`index.md`) pour informer les visiteurs que la leçon n'est pas maintenue/développée activement
  . Dans ces circonstances, considérez :

  1. en contactant [l'équipe administrative de l'incubateur] (mailto:incubator@carpentries.org) pour leur faire savoir que la leçon ne sera pas maintenue, et
  2. archivage du référentiel des leçons.

Si les développeurs souhaitent supprimer la leçon de l'incubateur The Carpentries
, le propriétaire du projet (un développeur ayant un accès administrateur) peut transférer le référentiel des leçons hors de l'organisation GitHub
de « carpentries-incubator\` via **Settings**-> \ **General**-> \ **Danger
Zone**-> \ **Transférer la propriété**.

## Espaces de communication et de collaboration

### Calendrier communautaire

Une fois planifiées, toutes les sessions de coworking pour le développement des leçons sont répertoriées sur
, notre [Calendrier communautaire
] (https://carpentries.org/community/events/). Vous pouvez ajouter des événements pertinents à votre calendrier personnel
à partir de là en cliquant sur
sur l'événement auquel vous souhaitez participer.

### Etherpad

The Carpentries utilise [Etherpad] (/resources/communications/etherpads.md) comme outil de prise de notes collaboratif lors d'ateliers, de formations et d'autres événements liés à la menuiserie. Vous trouverez ci-dessous une liste d'Etherpads pertinents pour le rôle de développeur de leçons.

- [Pad-of-Pads] (https://pad.carpentries.org/pad-of-pads) : Une liste de
  de nos Etherpads les plus couramment utilisés et d'autres ressources.
- [Notes de la session de coworking
  sur le développement de la leçon] (https://codimd.carpentries.org/lessondev-coworking) : informations d'inscription
  , détails de connexion et notes prises lors des sessions de coworking mensuelles
  (CodiMD),

### GitHub

- [Le référentiel
  des propositions de l'incubateur Carpentries] (https://github.com/carpentries-incubator/proposals) : un endroit
  permettant à la communauté The Carpentries de proposer de nouvelles leçons pour le développement de
  dans l'incubateur.
- [Le référentiel
  de The Carpentries Lab Reviews] (https://github.com/carpentries-lab/reviews) : un endroit
  où les développeurs de leçons peuvent soumettre leurs leçons pour une évaluation ouverte par les pairs et une acceptation
  à The Carpentries Lab.

### Slack

{{'[Rejoignez l'espace de travail Slack de The Carpentries] ({}) '.format (slack_invite)}}. Pour suivre les conversations relatives à ce rôle, vous devez rejoindre les canaux suivants :

- La chaîne #lesson -dev de l'espace de travail Slack de The Carpentries est une plateforme permettant à l'ensemble de la communauté de poser des questions et de participer à des discussions sur le thème de l'élaboration des leçons.
- Nous recommandons aux développeurs de leçons de parcourir les chaînes existantes dans l'espace de travail Slack
  , pour trouver celles qui sont pertinentes pour le sujet/le domaine de
  de leur leçon.
- Il peut également être utile de créer une nouvelle chaîne pour votre leçon, sous forme d'espace
  pour discuter du processus de développement avec vos collaborateurs,
  et pour que les membres de la communauté puissent poser des questions sur la leçon.

Si vous êtes nouveau sur Slack, notre {{"[Slack Guide] ({}) » .format (slack_guide)}} vous aidera à configurer votre profil et vous donnera un aperçu de la façon dont nous utilisons la plateforme au quotidien.

### Liste de diffusion

Vous pouvez accéder aux listes de diffusion de The Carpentries à l'adresse
[TopicBox] (https://carpentries.topicbox.com/latest). La
[liste de diffusion des développeurs de l'incubateur] (https://carpentries.topicbox.com/groups/incubator-developers)
est celle qui convient à l'exercice de ce rôle.

Pour rejoindre une ou plusieurs listes de diffusion de Carpentries, vous devez [créer un identifiant sur le site] (https://carpentries.topicbox.com/latest). Une fois cela fait, vous pouvez faire défiler la liste des groupes et cliquer sur « Rejoindre la conversation » (pour les envois ouverts) ou sur « Demander à participer » (pour les listes de diffusion nécessitant l'approbation de l'administrateur). Si vous utilisez Topicbox pour la première fois, veuillez consulter notre {{"[Topicbox Guide] ({}) » .format (topicbox_guide)}}.

## Guides étape par étape

### Utiliser les libellés des numéros pour promouvoir la collaboration

GitHub permet aux responsables d'un dépôt d'ajouter des informations contextuelles
aux Issues et aux Pull Requests sous forme de labels.
[The Carpentries utilise un ensemble étendu d'étiquettes de numéros dans ses référentiels de leçons] (../resources/curriculum/issue-labels.md).

Deux labels, utilisés par The Carpentries et dans de nombreux référentiels de GitHub,
peuvent être déployés pour augmenter la visibilité de votre leçon et encourager les membres de la communauté
à contribuer à son développement.

L'étiquette \*\* « help wanted » \*\* doit être utilisée pour mettre en évidence les problèmes liés à
pour lesquels vous souhaiteriez obtenir une aide supplémentaire. Le site web de Carpentries
comprend une [page Help Wanted
] (https://carpentries.org/help-wanted-issues/), qui peut
répertorier automatiquement tous les problèmes étiquetés « aide recherchée » sur les référentiels
provenant de The Carpentries, Software Carpentry, Data Carpentry, Library
Carpentry, CarpentriesLab et The Carpentries Incubator. Découvrez comment
peut inclure les problèmes de votre référentiel de leçons sur la page Help Wanted en passant en revue les [Informations pour les responsables de
] (https://carpentries.org/help-wanted-issues/#for-maintainers)
sur la page elle-même.

L'étiquette \*\* « bon premier numéro » \*\* doit être utilisée pour identifier les problèmes pour lesquels
constituerait un bon point d'entrée pour les nouveaux arrivants qui cherchent un moyen d'apporter
à votre leçon. Le travail nécessaire pour résoudre un problème avec cette étiquette
ne nécessite généralement pas une connaissance approfondie de la structure
ou des subtilités de votre référentiel de leçons, ni une compréhension experte
du contenu. L'étiquette « bon premier numéro » est tellement utilisée
que GitHub propose une page à l'adresse \ `[repository
URL] /contribute <https://github.com/swcarpentry/r-novice-gapminder/contribute>`__
pour chaque référentiel, répertoriant les problèmes liés à cette étiquette.

### Ajouter des balises de sujet à un référentiel de leçons

{{'[Official Lessons in The Carpentries Lesson Programs] ({}/lessons/) '.format (carpentries_website)}} sont répertoriés sur le site Web de The Carpentries, sur la base des métadonnées décrivant la leçon. Ces métadonnées sont ajoutées sous forme de balises thématiques dans le référentiel des leçons. Ces balises thématiques doivent être définies dès que possible après la création de la leçon ou son ajout à l'incubateur. Certaines sont essentielles et proviennent d'un ensemble limité de valeurs, tandis que d'autres sont plus flexibles. Le tableau ci-dessous fournit des indications sur les types et le nombre de balises thématiques que chaque référentiel de leçons doit avoir.

| Catégorie   | Exemple                    | Numéro | Descriptif                                                                                                                                                                                                          |
| ----------- | -------------------------- | ------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Leçon       | leçon                      | 1      | Doit être une leçon pour figurer sur la page des leçons développées par la communauté                                                                                                                               |
| Lieu        | menuiserie de données      | 1      | Une description du programme de leçon auquel appartient la leçon, avec des mots séparés par des tirets (c'est-à-dire menuiserie logicielle, menuiserie de données et menuiserie de bibliothèque) |
| Langue      | espagnol                   | > 0    | La ou les langues dans lesquelles la leçon est disponible                                                                                                                                                           |
| Étape       | écurie                     | 1      | Le stade de développement actuel de la leçon                                                                                                                                                                        |
| Domaine     | écologie microbienne       | 1 à 2  | Le ou les domaines de haut niveau de la leçon pour une catégorisation générale                                                                                                                                      |
| Outils      | python                     | 1 à 3  | Le ou les principaux outils enseignés dans la leçon                                                                                                                                                                 |
| Compétences | classification taxonomique | 1 à 3  | La ou les compétences principales enseignées dans la leçon                                                                                                                                                          |

L'équipe du programme vous aidera à définir les balises thématiques
appropriées pour votre leçon. Pour garantir la cohérence de tous les référentiels de leçons
développés par la communauté The Carpentries, veuillez vous référer
à [cette liste] (https://docs.google.com/spreadsheets/d/1KkmBtCu4PaNb5nzJAD82UHcfHQlaPY84qPVxw8WO8es/edit?usp=sharing)
des balises thématiques actuellement utilisées dans The Carpentries Incubator, et réutilisez
ces valeurs le cas échéant, en créant de nouvelles balises de sujet sans
étiquette préexistante pour votre leçon.

### [Comment organiser un sprint de développement de leçons] (/resources/curriculum/lesson-sprint-recommendations.md)

De nombreux développeurs de leçons trouvent utile d'organiser un événement dédié pour progresser et améliorer la collaboration sur leurs projets de cours.
Cette ressource fournit un ensemble de recommandations sur la manière d'organiser un sprint de développement de leçons efficace et inclusif.

### Promouvoir votre projet dans le cadre de The Incubator Lesson Spotlight

The Incubator Lesson Spotlight est un article régulier du blog et de la newsletter
de The Carpentries, mettant en lumière une leçon actuellement en cours de développement par la communauté
. L'objectif de la série Spotlight est d'accroître la visibilité
de cette leçon auprès de l'ensemble de la communauté et d'encourager les membres de la communauté
à contribuer au développement ultérieur de cette leçon
.

Toutes les leçons de [The Carpentries
Incubator] (https://github.com/carpentries-incubator/) peuvent être incluses dans la série
, quel que soit le stade de développement actuel de la leçon
. C'est un bon moyen pour les leçons des premiers stades
du développement d'attirer de nouveaux collaborateurs, et pour celles des étapes ultérieures
d'inviter d'autres personnes à revoir la leçon de manière informelle et à essayer
d'enseigner la matière. Pour soumettre votre leçon afin qu'elle figure dans la série
, suivez les étapes ci-dessous.

1. Réfléchissez à la manière dont vous pouvez préparer votre leçon pour les nouveaux contributeurs
   avant la publication de la fonctionnalité. Cela peut impliquer d'étiqueter les problèmes
   existants (par exemple pour qu'ils apparaissent sur [la page Help Wanted
   ] (https://carpentries.org/help-wanted-issues/)) ou d'en créer
   nouveaux, en vous assurant que votre fichier CONTRIBUTING.md est à jour, et/ou
   en planifiant la publication de la fonctionnalité Spotlight pour qu'elle corresponde à une période relativement calme de
   de votre emploi du temps afin de pouvoir répondre
   rapidement à tout nouveau problème et à toute demande d'extraction.
2. Remplissez le [formulaire
   de soumission du contenu de Incubator Lesson Spotlight] (https://docs.google.com/forms/d/e/1FAIpQLScJimGMtzqAFE-Tii-LvbfGZqtKj0OC4ken7_Qdlta8uZXAUA/viewform),
   en fournissant les détails de la leçon à inclure dans la fonctionnalité. Il peut être bénéfique de collaborer sur ce contenu avec d'autres développeurs
   travaillant sur la leçon.
   L'équipe principale de Carpentries utilisera le contenu
   fourni dans le formulaire pour créer un article pour [le blog The Carpentries
   ] (https://carpentries.org/blog/) et un article pour
   la [newsletter Carpentries Clippings] (https://carpentries.org/newsletter/).
3. Une fois le billet de blog rédigé, une pull request sera ouverte pour
   ajouter cet article au site Web. Vous serez tagué pour une révision (optionnelle)
   de cette pull request avant sa publication. Pour consulter le billet de blog
   , lisez le contenu de l'article et commentez le fil de discussion
   pour demander des modifications à la fonctionnalité.

### Soumettre une leçon à The Carpentries Lab

Le Carpentries Lab propose des leçons développées par la communauté qui ont été évaluées par des pairs
et sur lesquelles les instructeurs peuvent compter pour répondre à la norme
élevée de qualité et de stabilité. Le Lab fournit une plate-forme pour l'évaluation ouverte des leçons par les pairs
et pour promouvoir les leçons qui ont été intégrées à la collection
.

Pour soumettre une leçon à une évaluation par les pairs dans The Carpentries Lab, suivez ces étapes
 :

1. Vérifiez les [critères d'éligibilité pour les leçons à réviser dans le laboratoire
   ] (https://github.com/carpentries-lab/reviews#what-makes-a-lesson-a-good-candidate-for-the-carpentries-lab).
2. Ouvrez un nouveau numéro dans le [référentiel Reviews
   ] (https://github.com/carpentries-lab/reviews/issues/new?assignees=&labels=new-submission&template=submission.md&title=%5BREV%5D%3A+)
   et répondez aux questions du modèle de numéro pour informer les rédacteurs
   de la leçon.

### [Piloter une leçon] (/resources/curriculum/lesson-pilots.md)

Enseigner une leçon pour la première fois est très enrichissant, mais l'expérience des professeurs et des apprenants permet également d'aborder et de clarifier certaines parties du contenu.
Cela fait des enseignements précoces, que nous appelons _pilotes de leçon_, des étapes cruciales dans le développement d'une leçon de haute qualité.
Cette ressource fournit plus d'informations sur la manière de tester une nouvelle leçon dans le cadre d'ateliers, sur la manière dont ces ateliers pilotes s'alignent sur [le cycle de vie de la leçon] (/resources/curriculum/lesson-life-cycle.md), et des conseils sur la logistique, la collecte de commentaires pertinents, etc.

## Ressources

### [Présentation de The Carpentries Workbench] (https://carpentries.github.io/sandpaper-docs/)

Documentation pour The Carpentries Workbench, infrastructure open source
pour les sites Web de cours. La documentation explique comment installer le Workbench
afin que les développeurs de leçons puissent modifier et prévisualiser leurs leçons
sur leur propre ordinateur, comment initialiser une nouvelle leçon et utiliser les différents éléments
du modèle de leçon, et comment se tenir au courant avec
des dernières modifications apportées à l'infrastructure.

### [Programme de formation pour l'élaboration de leçons en collaboration] (https://carpentries.github.io/lesson-development-training/)

Une leçon conçue pour enseigner les compétences et les bonnes pratiques en matière de conception de leçons, de développement de sites Web de leçons
et de collaboration via GitHub. Les membres de la communauté
peuvent s'inscrire pour participer à cette formation et/ou suivre le programme en
à leur rythme.

### [Choisir un récit et un ensemble de données pour une leçon] (/resources/curriculum/narrative-example-data.md)

Conseils pour les concepteurs de leçons lorsqu'ils choisissent un récit pour leur leçon et exemples de données à y inclure.
Comprend des listes de points à prendre en compte lors du choix d'un jeu de données narratif et d'exemple, ainsi que des informations associées sur les licences et la publication de données.

### [Modèle de sondage de feedback sur l'atelier pilote] (https://docs.google.com/forms/d/1OGCQBotD2nOJkc7KpFZLhFfb3EBcxEDwHz_3p48qz3U/template/preview)

Les enquêtes standard de Carpentries avant et après les ateliers ne prennent pas en charge les leçons pilotes
. Vous devrez donc créer vos propres enquêtes pour envoyer
avant/après un atelier pilote. Bien que les enquêtes pour les ateliers pilotes incluent fréquemment des questions spécifiques à la leçon
en cours de projet pilote, certaines questions de feedback standard peuvent être posées
après un projet pilote afin d'évaluer la conception et le déroulement de la leçon.
Cette enquête
[modèle d'enquête post-atelier pilote
] (https://docs.google.com/forms/d/1OGCQBotD2nOJkc7KpFZLhFfb3EBcxEDwHz_3p48qz3U/template/preview)
peut être copiée et adaptée aux besoins de votre leçon, et partagée
avec les apprenants à la place de l'enquête standard post-atelier.

### [Ateliers pilotes de leçons] (/resources/curriculum/lesson-pilots.md)

Informations expliquant pourquoi et comment nous testons de nouvelles leçons dans le cadre d'ateliers, y compris des conseils et des modèles à utiliser pour les animateurs et les instructeurs des ateliers pilotes.

### Modèles d'annonces bêta

Un [article
sur le blog d'annonce bêta] (https://docs.google.com/document/d/1z8QmxDIiew-p1d8aLzXa0vt0FLUHNtK3oS3tucyrRsI/edit?usp=sharing)
et un [modèle d'annonce bêta par e-mail
] (https://docs.google.com/document/d/1hHnm-Ljb_o_rNd9bvQ83ilq40KoGoEfMPTSrFS4QOj8/edit?usp=sharing)
pour faire connaître la version bêta d'une leçon. Ils peuvent être utilisés pour appeler les membres de la communauté
à se porter volontaires pour animer un atelier pilote bêta afin de faciliter le développement continu de la leçon
.

### [Matériel d'intégration au programme] (/resources/curriculum/curriculum_onboarding.md)

Conseils pour l'élaboration de matériel qui aidera les professeurs à se préparer à enseigner votre nouvelle leçon ou votre nouveau programme.

### [Processus de publication des leçons] (/resources/curriculum/lesson-release.md)

Description de la façon de préparer un communiqué de leçon et de le publier sur Zenodo.

