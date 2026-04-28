# Le cycle de vie des leçons

**Remarque concernant les _instructeurs_ et les _instructeurs_ :** dans la majeure partie de ce manuel, nous faisons référence aux instructeurs, en majuscules pour indiquer qu'il s'agit d'un poste certifié au sein de la communauté, c'est-à-dire d'une personne qui a suivi la formation d'instructeur de menuiserie.
Certains contenus de notre manuel sur l'élaboration des programmes font référence aux formateurs (sans majuscules), afin de faire la distinction entre ceux qui enseignent un atelier mais qui ne sont peut-être pas encore des instructeurs certifiés.

La communauté Carpentries développe des leçons sous forme de projets Open Source : les leçons et leurs fichiers sources sont généralement disponibles en ligne dès les premiers stades de développement.
Il peut être utile pour les visiteurs d'une leçon (professeurs envisageant de l'enseigner, contributeurs potentiels explorant son contenu, etc.) et pour ses développeurs eux-mêmes, de pouvoir identifier rapidement l'état de développement d'une leçon.
L'élaboration des leçons est un processus itératif, dont le contenu et la conception sont toujours sujets à évolution et à amélioration.
Par exemple, lorsque des commentaires sont reçus lorsqu'une nouvelle leçon est enseignée, ou en réponse à de nouvelles fonctionnalités ou à d'autres changements dans son sujet.
Au fil du temps, le contenu devient généralement plus complet, plus précis, plus percutant et plus stable, les changements, en particulier les modifications majeures telles que la réorganisation ou l'ajout/la suppression de sections entières, devenant de moins en moins fréquents.

The Carpentries classe l'état de développement des leçons dans un système similaire à celui utilisé pour le développement de logiciels : nous les classons en fonction de leur maturité/stabilité, allant de _pre-alpha_ à _stable_.

! [Le modèle de cycle de vie de la leçon de menuiserie] (../../img/life_cycle.svg)

- **_Pre-alpha:_** la leçon en est aux premiers stades de la conception et du développement.
  Le contenu des leçons de la version pré-alpha est susceptible d'être incomplet et non testé, et peut subir des modifications majeures à tout moment. Cette étiquette est généralement appliquée à une leçon jusqu'à ce qu'une première ébauche soit terminée.
- **_Alpha:_** la leçon est pilotée par ses développeurs.
  Le contenu des leçons en version alpha a probablement été entièrement rédigé, mais on peut s'attendre à des lacunes, à des incohérences et à des erreurs.
  Ce label est généralement appliqué à une leçon une fois que sa première ébauche est terminée et avant que les premiers ateliers pilotes n'aient lieu.
- **_Beta:_** la leçon est prête à être pilotée par d'autres instructeurs.
  Le contenu des leçons en version bêta a été testé par (au moins) ses développeurs, et le contenu a été ajusté en fonction de cette expérience.
  Le contenu comprend des conseils pour les instructeurs sur la manière de l'enseigner efficacement.
  D'autres changements sont probables, car les commentaires provenant d'ateliers pilotes supplémentaires seront intégrés.
  Cette étiquette est généralement appliquée à une leçon lorsque ses développeurs sont convaincus qu'elle est prête à être utilisée dans des ateliers par d'autres professeurs.
- **_Stable:_** : la leçon a fait l'objet de tests approfondis et aucun changement majeur n'est attendu (sans avertissement significatif).
  Le contenu des leçons stables peut encore changer de temps à autre, mais les modifications sont généralement minimes et n'ont pas d'impact important sur la capacité du professeur à l'enseigner s'il connaît une version antérieure (stable).
  Cette étiquette est généralement appliquée à une leçon une fois que les commentaires des ateliers pilotes bêta ont été intégrés.

L'étape du cycle de vie d'une leçon est affichée bien en évidence en haut de la page sur les sites Web des leçons.
Il est également visible en tant que « sujet » sur le référentiel GitHub de la leçon, sous la case _About_ sur le côté droit de la page d'accueil du référentiel.

## Comment se déroule l'étape du cycle de vie ?

L'état du cycle de vie d'une leçon peut être ajusté en modifiant le paramètre life_cycle dans le fichier config.yaml de la leçon, ainsi que le sujet équivalent sur le référentiel GitHub source.

## Qui est responsable du choix de l'étape du cycle de vie d'une leçon ?

Pour les leçons organisées par la communauté dans The Carpentries Incubator, les concepteurs de leçons sont libres de choisir le label qui leur convient.
Les cours dispensés par la communauté dans The Carpentries Lab ont été évalués par les pairs et devraient être considérés comme stables.
L'étape du cycle de vie des leçons appartenant à un programme de cours de menuiserie doit être modifiée après consultation du comité consultatif du programme concerné et/ou de l'équipe chargée du programme.
La consultation est particulièrement importante avant de marquer une leçon comme étant bêta ou stable.

## Que se passe-t-il à chaque étape du cycle de vie ?

[Les ateliers pilotes] (lesson-pilots.md) sont probablement les événements les plus importants qui ont lieu avant qu'une leçon n'atteigne la stabilité.
Cependant, voici quelques autres actions que les développeurs de leçons peuvent prendre à différentes étapes :

- **Pré-alpha :**
  - [Soumettez la leçon à The Carpentries Incubator] (https://github.com/carpentries-incubator/proposals/).
  - Participez à [Formation à l'élaboration de leçons en collaboration] (https://carpentries.org/lesson-development-training).
  - Appel à collaborateurs.
  - Si vous souhaitez que la nouvelle leçon rejoigne un programme ou un programme de cours existant sur la menuiserie, consultez le [Comité consultatif du programme] (https://carpentries.org/curriculum-advisors/) ou le [Comité de gouvernance du programme de leçons] (https://carpentries.org/community/lesson_program_governors/) concerné dès que possible.
    Ces groupes de gouvernance communautaire peuvent fournir des commentaires sur vos projets et vous donner des conseils sur la manière de garantir une intégration réussie de la nouvelle leçon.
- **Alpha** : \*\*
  - Organisez [des ateliers pilotes alpha] (lesson-pilots.md#alpha-and-beta-pilots) et répétez la conception et le contenu de la leçon.
  - Faites connaître la leçon à la communauté The Carpentries.
- **Bêta :**
  - Trouvez des instructeurs qui peuvent enseigner la leçon dans le cadre des [ateliers pilotes bêta] (lesson-pilots.md#alpha-and-beta-pilots), et recueillez leurs commentaires pour améliorer encore la leçon.
    Envisagez d'inviter ces [instructeurs du pilote bêta] (./lesson-development-roles.md#beta-pilot-instructors) à rejoindre l'équipe chargée de développer et de maintenir la leçon.
  - [Publiez la leçon sur Zénodo et obtenez un DOI] (./lesson-release.md).
  - [Soumettez la leçon pour évaluation par les pairs dans The Carpentries Lab] (https://github.com/carpentries-lab/reviews/).
- **Stable :**
  - [Publiez la version stable sur Zenodo] (./lesson-release.md).
    - Vous souhaiterez peut-être répéter ce processus régulièrement, par exemple en publiant des publications annuelles.

! [Le modèle de cycle de vie de la leçon sur la menuiserie est annoté pour montrer plus de détails sur ce qui peut se passer à chaque étape du processus] (../../img/life_cycle_annotated.svg)
