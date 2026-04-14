# Rôles d'élaboration des leçons

**Remarque concernant les _instructeurs_ et les _instructeurs_ :** dans la majeure partie de ce manuel, nous faisons référence aux instructeurs, en majuscules pour indiquer qu'il s'agit d'un poste certifié au sein de la communauté, c'est-à-dire d'une personne qui a suivi la formation d'instructeur de menuiserie.
Certains contenus de notre manuel sur l'élaboration des programmes font référence aux formateurs (sans majuscules), afin de faire la distinction entre ceux qui enseignent un atelier mais qui ne sont peut-être pas encore des instructeurs certifiés.
Vous remarquerez peut-être également la même distinction entre les _mainteneurs_, qui ont terminé l'intégration des mainteneurs et s'occupent d'une leçon officielle de menuiserie, et les _mainteneurs_, qui s'occupent des leçons communautaires.

La création d'une nouvelle leçon ou d'un nouveau programme est un processus collaboratif, impliquant généralement de nombreux membres de la communauté assumant différents rôles. Il s'agit également d'un [processus itératif] (./lesson-life-cycle.md), ce qui signifie qu'une leçon peut toujours être considérée comme étant en cours de développement dans une certaine mesure.

Cette page décrit les différents rôles que les utilisateurs peuvent jouer dans la conception, le développement, les tests et la maintenance d'une nouvelle leçon ou d'un nouveau programme.

- [Développeurs de leçons] (#lesson-developers)
- [Instructeurs de l'atelier pilote] (#pilot-workshop-instructors)
  - [Instructeurs Alpha Pilot] (#alpha-pilot-instructors)
  - [Instructeurs pilotes bêta] (#beta-pilot-instructors)
- [Mainteneurs] (#maintainers)
- [Réviseurs] (#reviewers)

## Développeurs de leçons

Une leçon peut avoir un ou plusieurs développeurs initiaux. Les développeurs rédigent le contenu, les figures et le code de la leçon et créent des problèmes de défi appropriés. L'équipe de développeurs devrait avoir à la fois une expérience du domaine appropriée (travaillant dans le même domaine que le public cible des matériaux) et une expérience programmatique, en utilisant régulièrement les outils pour lesquels elle développe des leçons dans son propre travail. D'un point de vue technique, les développeurs de leçons devront également se familiariser avec l'infrastructure que nous utilisons pour développer et héberger les leçons de The Carpentries : principalement git, GitHub et Markdown et/ou R Markdown. Si vous n'êtes pas à l'aise avec l'un ou l'ensemble de ces outils, certaines des ressources répertoriées ci-dessous peuvent être utilisées pour les apprendre et les utiliser.

La rédaction d'une leçon n'est qu'une partie du processus de développement : les nouvelles leçons doivent être testées de manière approfondie dans le cadre d' [_ateliers pilotes_] (lesson-pilots), ajustées en fonction des commentaires, puis mises à jour et maintenues à long terme. [Ce cycle de vie d'une leçon est abordé plus en détail ailleurs dans ce manuel] (lesson-life-cycle.md).

### Ressources pour les développeurs de leçons

- Notre [Formation collaborative pour le développement des leçons] (https://carpentries.github.io/lesson-development-training/) enseigne les principes et les bonnes pratiques en matière de conception et de développement de programmes, ainsi que des compétences de collaboration pour aider l'équipe chargée de l'élaboration des leçons à travailler ensemble efficacement. Il présente également les principes fondamentaux de la création de contenu de cours accessible avec The Carpentries Workbench, les outils que nous utilisons pour créer des sites Web de leçons à partir de fichiers sources d'un référentiel GitHub.
- [Introduction à The Carpentries Workbench] (https://carpentries.github.io/sandpaper-docs/) fournit une documentation plus complète sur l'infrastructure des leçons.
- [Une introduction à Markdown et GitHub] (https://carpentries.github.io/lesson-development-training/instructor/markdown-github-primer.html) renvoie à deux ressources qui enseignent les principes fondamentaux de deux outils essentiels au développement des leçons dans The Carpentries.

## Instructeurs de l'atelier pilote

Nos leçons sont principalement destinées à être enseignées dans le cadre d'ateliers, et leur conception et leur contenu doivent être testés dans ce cadre. Les commentaires doivent être recueillis pendant l'atelier et intégrés à la leçon. Nous appelons _ateliers pilotes_ les événements au cours desquels une nouvelle leçon est testée.
[La section Ateliers pilotes de ce manuel] (lesson-pilots) fournit plus d'informations sur ces événements, y compris des modèles et des conseils sur la logistique des événements.

### Instructeurs Alpha Pilot

Il est courant, mais ce n'est pas essentiel, que les instructeurs du premier projet pilote d'une nouvelle leçon soient les développeurs de la leçon d'origine. Nous appelons ces événements _alpha pilots_ et ils constituent une excellente occasion de recueillir des informations et d'obtenir des commentaires précoces afin d'éclairer le développement futur du contenu. En plus de recueillir les commentaires des apprenants, les instructeurs du projet alpha pilot devraient prendre de nombreuses notes pendant l'événement. Nous recommandons aux instructeurs pilotes de se rencontrer dès que possible après l'atelier, ou à la fin de chaque session d'enseignement, pour faire le point sur leur expérience et préparer une liste de points d'action que les concepteurs de leçons devront aborder pour améliorer la leçon.

### Instructeurs Beta Pilot

Si l'adoption de la nouvelle leçon dans le programme officiel de The Carpentries est envisagée, les instructeurs de ces ateliers pilotes bêta doivent être des instructeurs de menuiserie certifiés ayant déjà enseigné au moins deux ateliers de menuiserie. Les formateurs possédant ce niveau d'expérience seront mieux préparés à résoudre les problèmes survenant pendant l'atelier et plus susceptibles de fournir des commentaires utiles après l'atelier. Les instructeurs certifiés ne sont pas requis pour les pilotes bêta de leçons qui ne deviendront pas le programme officiel de menuiserie.

Les instructeurs du pilote bêta peuvent être des mainteneurs, des conseillers pédagogiques ou tout autre membre de la communauté Carpentries autre que les développeurs des leçons d'origine. En fait, le recrutement d'instructeurs pilotes bêta qui jouent déjà un rôle actif dans la leçon risque d'être fructueux, car ces personnes sont investies dans la maturation de la leçon. Pour deux ateliers pilotes bêta, vous aurez besoin d'au moins quatre instructeurs. Les auteurs des leçons devraient prévoir de rencontrer virtuellement les instructeurs pilotes avant l'atelier pour répondre aux questions et fournir toute aide technique concernant la configuration.

### Ressources pour les instructeurs des ateliers pilotes

- [La section Ateliers pilotes de ce manuel] (lesson-pilots) comprend plus d'informations sur l'objectif des leçons pilotes, des conseils pour les développeurs et les animateurs de leçons, des modèles pour les communications et les enquêtes de satisfaction, etc.
- L'épisode [Preparing to Teach] (https://carpentries.github.io/lesson-development-training/preparing.html) de Collaborative Lesson Development Training fournit des conseils aux développeurs de leçons qui planifient des pilotes alpha pour une nouvelle leçon.

## Mainteneurs

Les mainteneurs de leçons sont essentiels à la viabilité à long terme d'une leçon. Au fur et à mesure qu'une leçon est enseignée, les professeurs et les apprenants identifient les points à améliorer, qu'il s'agisse de corriger une faute de frappe, de simplifier le code ou de suggérer un changement significatif dans le récit d'une leçon. Les responsables surveillent de manière proactive le référentiel GitHub de leur leçon pour s'assurer que les problèmes et les suggestions d'amélioration sont traités en temps opportun. Les mainteneurs jouent également un rôle essentiel dans la communication avec les contributeurs, en veillant à ce que notre communauté soit à la hauteur de ses idéaux en accueillant et en appréciant les contributions de tous, des nouveaux contributeurs aux membres de longue date de la communauté The Carpentries.
Les personnes agissant en tant que mainteneurs doivent avoir de l'expérience avec les outils enseignés dans la leçon, idéalement en les utilisant quotidiennement ou chaque semaine dans leur propre travail. En outre, ils doivent avoir de l'expérience dans un domaine pertinent lié à la leçon, et/ou une expérience de travail avec GitHub et les autres technologies que nous utilisons pour créer et héberger nos leçons. Chaque leçon doit avoir au moins deux responsables, et il est avantageux pour ces derniers d'avoir des niveaux d'expérience variés en ce qui concerne le domaine et les aspects techniques de la leçon, ainsi que les outils de maintenance.

### Ressources pour les mainteneurs

- Le [Manuel des mainteneurs] (../../handbooks/maintainers.md) comprend des conseils sur les communications, la gestion du référentiel de leçons et d'autres aspects du rôle.
- Le [Programme d'intégration des mainteneurs] (https://carpentries.github.io/maintainer-onboarding/) contient les informations que nous fournissons aux mainteneurs pour les cours officiels de menuiserie lorsqu'ils entrent en fonction.
- [Introduction à The Carpentries Workbench] (https://carpentries.github.io/sandpaper-docs/) fournit une documentation plus complète sur l'infrastructure des leçons : les outils que nous utilisons pour créer des sites Web de leçons à partir des fichiers sources d'un référentiel GitHub.

## Conseillers des programmes

(Bien que les conseillers pédagogiques puissent être très utiles pour l'élaboration de toute nouvelle leçon/programme, ils ne sont requis que pour le programme officiel de menuiserie.)

Alors que les concepteurs et les mainteneurs de leçons s'occupent de l'amélioration et de la maintenance quotidiennes des leçons, les conseillers pédagogiques fournissent des conseils de niveau supérieur sur l'orientation de ce développement. Les conseillers pédagogiques doivent être des experts dans le domaine de la leçon et être conscients de la manière dont les compétences enseignées sont (ou doivent être) appliquées dans ce domaine. Les conseillers en programmes ont la responsabilité de guider l'élaboration d'un [programme] complet (./curriculum-structure.md) : lorsque ce programme comprend plusieurs leçons, les conseillers en programmes doivent réfléchir à la manière dont il doit être développé dans son ensemble et à l'impact des modifications apportées à une leçon sur les autres.

Si une nouvelle leçon est destinée à être intégrée à un programme existant, les concepteurs de leçons doivent consulter le comité consultatif du programme existant au sujet de leurs plans le plus tôt possible dans le processus de développement. Par exemple, les développeurs de leçons peuvent partager un aperçu de la conception et du contenu prévus de la leçon avant d'investir beaucoup de temps dans la création du matériel. Cette consultation précoce permet aux conseillers pédagogiques de commenter la leçon prévue, d'évaluer dans quelle mesure elle s'intégrera facilement au programme existant et de réfléchir à l'impact qu'elle pourrait avoir sur les autres leçons du programme.

### Ressources pour les conseillers en matière de programmes

Le [Manuel des conseillers en matière de programmes] (/handbooks/curriculum_advisors.md) contient plus d'informations sur le rôle, la logistique de la gestion des comités consultatifs sur les programmes, etc.

## Réviseurs

La rétroaction est essentielle à l'élaboration d'une leçon efficace. L'objectif principal des [ateliers pilotes] (lesson-pilots.md) est de fournir des commentaires que les développeurs peuvent utiliser pour améliorer la conception et le contenu de leur nouvelle leçon. À cet égard, les formateurs participant aux ateliers pilotes peuvent être considérés comme des évaluateurs importants, en particulier ceux qui dirigent et fournissent des commentaires sur les pilotes bêta. Néanmoins, il peut être utile de solliciter des commentaires supplémentaires de la part des évaluateurs. Les évaluateurs doivent axer leur évaluation d'une leçon sur son utilité en tant que ressource d'apprentissage et d'enseignement accessible, sur son adéquation avec son public cible et sur l'exactitude de son contenu.
Les concepteurs de leçons peuvent trouver des réviseurs via leurs propres réseaux ou en communiquant avec l'ensemble de la communauté pour appeler des volontaires. Les réviseurs peuvent fournir des commentaires et suggérer des améliorations directement, sous la forme de problèmes et de demandes d'extraction sur le référentiel des leçons, ou par e-mail/discussion. The Carpentries héberge également une plateforme d'évaluation structurée et ouverte des leçons par les pairs par la communauté.

### Évaluation ouverte par les pairs des leçons du laboratoire de menuiserie

[The Carpentries Lab] (https://carpentries-lab.org/) propose des leçons gérées par la communauté qui ont été évaluées par les pairs et fournit une plate-forme pour le processus d'évaluation par les pairs.
Les évaluations existent sous forme de discussions sur des problèmes visibles par le public sur [le référentiel Lab Reviews] (https://github.com/carpentries-lab/reviews/). Les membres de la communauté The Carpentries se portent volontaires en tant que réviseurs et éditeurs pour le laboratoire.

### Ressources pour les évaluateurs

- La documentation du référentiel Carpentries Lab Reviews fournit [plus d'informations sur le processus d'évaluation par les pairs] (https://github.com/carpentries-lab/reviews?tab=readme-ov-file#what-is-the-process-for-submitting-a-lesson-to-the-carpentries-lab) et [les conseils fournis aux évaluateurs] (https://github.com/carpentries-lab/reviews/blob/main/docs/reviewer_guide.md).
- The Carpentries [Collaborative Lesson Development Training] (https://carpentries.github.io/lesson-development-training/) fournit des conseils sur les meilleures pratiques en matière de conception de leçons et de développement de contenu, qui peuvent être utilisées pour éclairer les révisions des leçons.

