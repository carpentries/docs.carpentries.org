# Création d'un référentiel de leçons Workbench

Suivez ces étapes pour vous aider à effectuer la configuration lorsque vous créez un référentiel de leçons sur GitHub qui utilise [The Carpentries Workbench] (https://carpentries.github.io/workbench/).

1. [Activer les flux de travail GitHub Actions] (#enable-the-github-actions-workflows)
2. [Activer les pages GitHub] (#activate-github-pages)
3. [Configurer les flux de maintenance] (#configure-maintenance-workflows)
4. [Obtenir de l'aide] (#getting-help)

## Activez les flux de travail GitHub Actions

Les actions sont désactivées par défaut dans les référentiels bifurqués.
Si vous souhaitez créer un site Web de cours à partir des fichiers de votre fork, vous devez les activer.
\*\*Vous devez effectuer cette opération avant d'activer GitHub Pages sur le référentiel. \*\*

1. Pour activer GitHub Actions, accédez à l'onglet _Actions_ de votre référentiel.
   Vous devriez trouver un bouton « Comprenez mes flux de travail, allez-y et activez-les » _, sur lequel vous pouvez cliquer.
   Cela devrait alors afficher une page avec les flux de travail pour le référentiel répertoriés sur le côté gauche.
2. Trois des flux de travail répertoriés dans cette barre latérale gauche sont prévus pour être exécutés chaque semaine et seront toujours désactivés.
   Pour activer la création de sites Web de leçons, sélectionnez le flux de travail appelé « 01 Build and Deploy Site », puis _Enable workflow_ en haut à droite de la fenêtre.
3. Pour exécuter le flux de travail de création du site de la leçon pour la première fois, sélectionnez le menu déroulant _Exécuter le flux de travail_ (où le bouton _Activer le flux de travail_ se trouvait à l'étape 2), puis le bouton _Exécuter le flux de travail_.
   Le processus de construction prendra quelques minutes, après quoi la branche gh-pages de votre référentiel sera créée/mise à jour pour contenir la dernière version du site Web de la leçon.
   Vous pouvez désormais [activer les pages GitHub] (#activate-github-pages) pour diffuser les fichiers de cette branche sur Internet.
4. Si vous souhaitez configurer les exécutions hebdomadaires du flux de travail qui peuvent ouvrir automatiquement des demandes d'extraction pour mettre à jour l'infrastructure des leçons et le cache des packages (leçons R Markdown uniquement), vous devez répéter l'étape 2 ci-dessus pour les deux autres flux de travail désactivés, appelés « 02 Maintain : Mettre à jour les fichiers de flux de travail » et « 03 Maintain : Mettre à jour le cache des packages ».
   Une fois ces flux de travail activés, vous devrez [effectuer certaines configurations supplémentaires, décrites ci-dessous] (#configure-maintenance-workflows), pour qu'ils s'exécutent correctement.

## Activer les pages GitHub

\*\*Après avoir activé vos flux de travail GitHub Actions (voir ci-dessus) \*\*, vous pouvez configurer GitHub Pages pour diffuser votre site de cours à partir de la branche `gh-pages` de votre référentiel.

1. Ouvrez l'onglet _Paramètres_ de votre référentiel de leçons, puis accédez à _Pages_ sous _Code et automatisation_ dans la barre latérale gauche.
2. Dans _Build and deployment_, maintenez _Deploy from a branch_ sélectionné et choisissez `gh-pages` dans le menu déroulant sous _Branch_.
3. Cliquez sur _Save_.
4. Revenez à la première page (onglet _Code_) de votre répertoire de leçons et sélectionnez le symbole de la roue dentée en haut à droite de la section _À propos_.
   Cochez la case _Utiliser votre site web GitHub Pages_ pour afficher l'URL du site web de la leçon créé à partir de votre fork.

## Configuration des flux de maintenance

Lorsqu'ils sont configurés correctement, les deux flux de maintenance, « 02 Maintain : Update Workflow Files » et « 03 Maintain : Update Package Cache », peuvent créer des demandes d'extraction sur votre référentiel pour maintenir l'infrastructure des leçons et (si votre leçon utilise des fichiers sources R Markdown) les packages utilisés dans la leçon à jour à mesure que de nouvelles versions sont publiées.
Pour que cela fonctionne, vous devez créer un jeton d'accès qui permettra aux flux de travail d'ouvrir des pull requests en votre nom.

1. Ouvrez <https://github.com/settings/tokens/new> et entrez le nom `Sandpaper Token (<your github repository name>) `pour votre jeton, par exemple `Sandpaper Token (carpentries/lesson-development-training)`
2. Choisissez une durée de vie pour le jeton.
   Pour des raisons de sécurité, nous vous recommandons de ne pas choisir _Pas d'expiration_. Mais **si vous suivez l'étape ci-dessous**, le jeton ne peut être utilisé que pour effectuer un nombre très limité de tâches sur votre référentiel, vous n'avez donc pas nécessairement besoin de choisir une durée de vie très courte non plus.
3. Sous _Select scopes_, cochez la case correspondant à la portée _workflow_. (Cela entraînera également la vérification de toutes les étendues _repo_.)
4. Sélectionnez _Générer un token_.
5. Votre nouveau jeton d'accès personnel sera affiché, avec un bouton à côté qui peut être utilisé pour le copier dans votre presse-papiers.
   Copiez le jeton et revenez à l'onglet _Paramètres_ de votre référentiel de leçons.
   Sous _Sécurité_ dans la barre latérale gauche, ouvrez la liste déroulante _Secrets et variables_ et choisissez _Actions_.
6. Entrez `SANDPAPER_WORKFLOW` comme nom et collez votre jeton dans le champ _Value_.
7. Sélectionnez _Ajouter un secret_ pour terminer la configuration.

## Obtenir de l'aide

Si vous rencontrez des difficultés avec l'une de ces étapes, vous pouvez demander de l'aide en :

- Publier sur les chaînes `#workbench` et/ou `#lesson -dev` de Slack ({{'[Rejoignez l'espace de travail Slack de The Carpentries] ({}) '.format (slack_invite)}}).
- [Contacter l'équipe du programme par e-mail] (mailto:curriculum@carpentries.org).
- Ouvrez un problème sur votre référentiel, décrivez le problème que vous avez rencontré et ajoutez la balise `@tobyhodges`.

Pour aider les autres à résoudre votre problème, veuillez inclure une URL vers votre référentiel bifurqué dans votre message.
