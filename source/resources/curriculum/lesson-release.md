# Releasing a Lesson
**Note that Maintainers of Data Carpentry, Library Carpentry, and Software Carpentry lessons should not make lesson releases for now.**
The Curriculum Team will coordinate this process in the coming months.

Making regular releases of your lesson gives you and your contributors an opportunity to celebrate the improvements that have been made, and make it easier for them to receive credit and recognition for the work they have put in.
It is particularly important to release the lesson when it reaches key milestones in its development, e.g. before [beta pilot workshops](lesson-pilots.md) or when it reaches [a stable state](./lesson-life-cycle.md).

If you [publish the lesson on Zenodo](#publishing-the-lesson-on-zenodo) when you release it, you will receive a Digital Object Identifier that you and others can use to refer to the lesson and/or a particular version.
Publishing the lesson makes it more findable by other people, and -- if you include your [ORCID iD](https://info.orcid.org/what-is-orcid/) identifier in the information about its authors -- helps you list the project on your public profile.

## Preparing for a release

### Updating citation information
Lesson repositories can contain citation information in [Citation File Format](https://citation-file-format.github.io/).
The Collaborative Lesson Development Training curriculum includes [some discussion of why you should include this file in your lesson repository](https://carpentries.github.io/lesson-development-training/collaborating-newcomers.html#helping-people-cite-your-lesson).
The Carpentries Workbench documentation describes in more detail [how the file can be included in the repository](https://carpentries.github.io/sandpaper-docs/editing.html#making-your-lesson-citable) and gives an example.

We recommend that you keep citation information updated as you progress with lesson development and maintenance.
At the very least, you should ensure that the information in your `CITATION.cff` is current before releasing a new version of your lesson because this will simplify the process of releasing it to Zenodo.

## Publishing the lesson on Zenodo

* First, create a [Zenodo](https://zenodo.org/) account if you do not already have one, linked to your GitHub credentials
* Log into Zenodo and select 'GitHub' from the dropdown menu at the top-right
* On that page, find the name of your lesson repository in the listing and turn the switch 'On' to activate the Zenodo/GitHub integration
* [Make a release of your lesson](https://docs.github.com/en/repositories/releasing-projects-on-github/managing-releases-in-a-repository#creating-a-release) from its GitHub repository
* This will create a Zenodo record from that release.
  Zenodo will update this record with a new version every time you make another release from your lesson repository. 
* Edit the Zenodo entry to adjust anything that is not right.
  For example, the presence of a `CITATION.cff` file in your repository will make Zenodo think this is a record describing software.
  You can correct this to 'Lesson' in the _Resource Type_ field.
* Add the DOI for your record to the `README.md` and `CITATION.cff` files in your lesson repository.
  The record created from your release will include two DOIs: one for the specific version released this time, and a second 'top level' DOI that will always resolve to the latest version of the lesson released. 
  We recommend that you add the 'top-level' DOI to the files in your lesson repository. Zenodo gives you Markdown code to display a 'badge' icon e.g. ![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.8415001.svg) on your repository README. 
  Look for the DOI field in the _Details_ box on the right of the record page to find your badge.

