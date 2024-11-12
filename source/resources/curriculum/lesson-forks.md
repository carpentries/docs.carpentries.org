# Forking a Workbench Lesson Repository
Follow these steps to help you get setup when you fork a lesson repository on GitHub that is using [The Carpentries Workbench](https://carpentries.github.io/workbench/).

1. [Enable the GitHub Actions workflows](#enable-the-github-actions-workflows)
1. [Activate GitHub Pages](#activate-github-pages)
1. [Configure Maintenance Workflows](#configure-maintenance-workflows)
1. [Getting Help](#getting-help)

## Enable the GitHub Actions workflows
Actions are disabled by default in forked repositories. 
If you want a lesson website to be built from the files in your fork, you will need to activate them.
**You must do this before activating GitHub Pages on the repository.**

1. To enable GitHub Actions on, navigate to the _Actions_ tab of your repository. 
You should find a button saying _"I understand my workflows, go ahead and enable them"_, which you can click.
This should then display a page with the workflows for the repository listed on the left-hand side.
2. Three of the workflows listed in that left sidebar are scheduled to run weekly, and will still be disabled.
To enable lesson website builds, select the workflow called `01 Build and Deploy Site` and then _Enable workflow_ near the top right of the window.
3. To run the lesson site build workflow for the first time, select the _Run workflow_ drpdown (where the _Enable workflow_ button was in step 2) and then the _Run workflow_ button.
The build process will take a few minutes, after which the `gh-pages` branch of your repository will be created/updated to contain the latest version of the lesson website.
You can now [activate GitHub Pages](#activate-github-pages) to serve the files in that branch to the internet.
4. If you want to configure the weekly workflow runs that can automatically open pull requests to update the lesson infrastructure and package cache (R Markdown lessons only), you should repeat step 2 above for the two other disabled workflows, called `02 Maintain: Update Workflow Files` and `03 Maintain: Update Package Cache`.
After those workflows have been activated, you will need to [complete some additional configuration, described below](#configure-maintenance-workflows), before they will run successfully.


## Activate GitHub Pages
**After you have activated your GitHub Actions workflows (see above)** you can set up GitHub Pages to serve your lesson site from your repository's `gh-pages` branch.

1. Open the _Settings_ tab of your lesson repository, then navigate to _Pages_ under _Code and automation_ in the left sidebar.
2. Under _Build and deployment_, keep _Deploy from a branch_ selected, and choose `gh-pages` from the dropdown menu under _Branch_.
3. Click _Save_.
4. Return to the front page (_Code_ tab) of your lesson repository, and select the gear wheel symbol at the top right of the _About_ section.
Check the _Use your GitHub Pages website_ box, to display the URL of the lesson website built from your fork.


## Configure Maintenance Workflows
When configured appropriately, the two maintenance workflows, , can create pull requests on your repository to keep the lesson infrastructure and (if your lesson uses R Markdown source files) the packages used in the lesson up to date as new versions are released. 
For this to work, you need to create an access token that will allow the workflows to open pull requests on your behalf.

1. Open <https://github.com/settings/tokens/new> and enter the name `Sandpaper Token (<your github repository name>)` for your token, e.g. `Sandpaper Token (carpentries/lesson-development-training)`
1. Choose a lifespan for the token. 
For security, we recommend that you do not choose _No expiration_. But **if you follow the step below** the token can only be used to perform a very limited number of tasks on your repository, so you do not necessarily need to choose a very short lifespan either.
1. Under _Select scopes_, check the box for the _workflow_ scope. (This will cause all of the _repo_ scopes to also be checked.)
1. Select _Generate token_.
1. Your new personal access token will be displayed, with a button next to it that can be used to copy the token to your clipboard. 
Copy the token and return to the _Settings_ tab of your lesson repository.
Under _Security_ in the left sidebar, open the _Secrets and variables_ dropdown and choose _Actions_.
1. Enter `SANDPAPER_WORKFLOW` as the name, and paste your token into the _Value_ field.
1. Select _Add secret_ to complete the configuration.

## Getting Help
If you run into trouble with any of these steps, you can ask for help by:

* Posting to the `#workbench` and/or `#lesson-dev` channels on Slack ({{'[Join The Carpentries Slack workspace]({})'.format(slack_invite)}}).
* [contact the Curriculum Team by email](mailto:curriculum@carpentries.org).
* open an issue on your repository, describing the problem you have encountered, and tag `@tobyhodges`.

To help others troubleshoot your issue, please include a URL to your forked repository in your message.