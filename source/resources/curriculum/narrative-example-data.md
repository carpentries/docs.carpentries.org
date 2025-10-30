# Choosing a Narrative and Dataset for a Lesson
Writing your lesson as a story helps learners stay motivated and engaged, and can prevent you from making leaps from one topic to the next without covering a step that learners will find to be important later.
The narrative you create can also help learners more easily connect how the skills they are learning now could be useful after the workshop.
You can enable learners to make connections between what they learn in your lesson and their own work, by creating a narrative that resembles a situation the learners might encounter there.

For a lot of lessons developed in The Carpentries community, the narrative is closely tied to the example data used in the lesson.
A good example dataset makes it easier to teach the relevant skills, helps learners manage their cognitive load by focusing on what is most important.
Just like the narrative, finding the right dataset involves striking a balance between authenticity and clarity.

## Top Tips: Lesson Narrative

1. When choosing a narrative, consider:
    * Complexity: how easy will it be for learners to follow the narrative of the lesson?
    * Order: when should you introduce each of the key concepts to manage cognitive load most effectively?
      Could you sacrifice some realism to keep things simple at the beginning? 
      How can you position [the most important things as early as possible](https://www.youtube.com/watch?v=fQ4t7p6ZXDg) in the lesson?
    * Authenticity: will learners be able to relate to the story being told and the examples being used?
    * Efficiency: can you avoid or remove tangents and "side quests" that might distract learners (and instructors) from the lesson's objectives?
1. Devote time at the beginning of the lesson for a short introduction to the narrative. 
   An effective introduction should help learners understand how the story relates to their work, the problems they encounter, and the things they want to do with the skills they will learn.
1. Make use of images and figures to enhance your narrative.
   [Consider the licensing and terms of reuse on those images](#finding-images), and respect the intellectual property rights of image creators.
   Images can be distracting when they appear in the wrong place or are irrelevant or contradictory to the lesson content they accompany.
1. A single narrative throughout the lesson is often preferable but can be difficult to achieve.
   Use multiple, mini narratives for individual or groups of episodes if you need to.
   Where you wish for learners to develop understanding of more abstract concepts, [provide a variety of examples with a common theme](https://neverworkintheory.org/2022/05/25/brown-mind-learns.html).
   This could be achieved by providing multiple opportunities to recognise and apply the concept in taught examples, activities, and exercises.
1. Look for example data that will support your chosen narrative (see below).

### Examples of Lesson Narratives

* [Software Carpentry Git lesson](https://swcarpentry.github.io/git-novice/index.html) uses the story of Alfredo, a chef working with his team to create a repository of his favorite recipes.
* [Building Websites With Jekyll and GitHub lesson](https://carpentries-incubator.github.io/jekyll-pages-novice/filters/index.html) 
  uses the narrative of creating a website for a research project to teach authoring webpages with Markdown and compiling them into a website served on GitHub.
* [Building Better Research Software](https://carpentries-incubator.github.io/better-research-software/) uses the narrative of a poorly designed software project 
  (which analyses [NASA’s open data on spacewalks](https://data.nasa.gov/Raw-Data/Extra-vehicular-Activity-EVA-US-and-Russia/9kcy-zwvn/data_preview) undertaken by astronauts from 1965 to 2013) that over the course of the lesson gets improved in terms of code accessibility, readability, correctness and reusability.
  
### Finding Images
Copying an image from a website is technologically simple but can be legally and ethically complex.
Images are intellectual property and are subject to intellectual property laws including, but not limited to, copyright and trademark laws.
These laws differ by country but are consistent in theme: do not use intellectual property that does not belong to you without permission.

When looking for images that illustrate the narrative of your lesson, avoid copying images that do not include a reuse license.
Assume that you cannot reuse these images unless you seek written permission from the image creator or owner.
Instead, look for images that indicate that they are in the public domain or carry a permissive reuse license such as CC0 or CC-BY.
Public domain images can be freely reused and adapted.
Images carrying a reuse license can be used and adapted in accordance with their license terms.

If you cannot find reusable images that match your narrative, you can create your own images or seek help from others in the Carpentries community.
When incorporating original images into your lesson, be sure to license these images to be [compatible with the license](#compatible-licenses) on the rest of your lesson materials.

The guidance in this section is not a substitute for legal advice.

#### Compatible Licenses
Creative Commons offers a chart that identifies which CC licenses are compatible with each other for adaptation ("remix") purposes:
[Creative Commons license comparison chart](https://creativecommons.org/faq/#can-i-combine-material-under-different-creative-commons-licenses-in-my-work).

GNU offers commentary about a variety of licenses for free software; this resource may be valuable when considering a license for code:
[GNU: Various Licenses and Comments about Them](https://www.gnu.org/licenses/license-list.en.html).

::::::::::::::::::

## Top Tips: Example Datasets

1. Consider:
    * Authenticity: will your learners feel that the example data is representative of the kind of data they are/will be working with?
    * Size: data sets are often (very) large in modern data science and research. 
      Large example data sets may feel more authentic to learners, and help you illustrate important concepts and skills in your lesson.
      But larger datasets typically take longer to process, which may mean more time waiting for things to run during a workshop.
      They also place higher demands on learners' time and equipment, for downloading, storing, and processing files.
    * Complexity: keeping example data too simple may not prepare learners for what they will encounter after the workshop.
      However, data that is too complex will make it more difficult to manage cognitive load during the workshop.
    * Messiness: real data is often messy, and using example data that has been extensively sanitised or synthesised wholesale may not prepare learners for this.
      However, data cleaning can be time-consuming, reducing the space available for learners to explore other skills and concepts in the workshop.
1. Many of the points above are in contradiction to each other, and choosing the right dataset usually involves finding an acceptable balance between them.
   Some lesson developers choose to create their own example data: generating or synthesising your own example data provides a degree of control that is unavailable when resuing existing, real data, but may come at the cost of reduced authenticity.
   Others modify existing data, e.g. by subsampling or selecting a subset of variables and tables from the full, published dataset.
   If you do this, make sure to document the changes made to ensure reproducibility.
1. Also consider licensing: has the data provider granted permission for you to freely use it in your lesson and workshops?
   The best option is a dataset with a CC0 (Public Domain Dedication) license, as other licenses may have ambiguity around data reuse.
   If you'd like to learn more about CC0 and CC-BY licensing in relation to data, refer to Katie Fortney's excellent [blogpost on why CC-BY is not always a good fit](https://osc.universityofcalifornia.edu/2016/09/cc-by-and-data-not-always-a-good-fit/).
   Lessons included in [The Carpentries Incubator][carpentries-incubator] are encouraged to use CC0 licensed data, and may be required to do so to qualify for peer review in [The Carpentries Lab][carpentries-lab].
   Even with data in the public domain, please follow best practice and give attribution to the data provider or collecting agency.
1. Look for example data in public repositories.
   Data is often uploaded and published to [domain-specific or generalist repositories](#examples-of-public-repositories).
   If you create or modify your own data to use an example in your lesson, consider uploading and publishing it (with a CC0 license) for others to re-use.
1. It is also essential to think about data privacy: is there any potentially identifiable information included in the data? 
   If so, how could you remove it?
1. Data is commonly misused from historically excluded and exploited groups.
   When choosing a dataset, ensure that the data was collected with permission from the groups or individuals included.
   Consider whether the data could be upsetting to learners in a workshop.
   The [CARE Principles for Indigenous Data Governance](https://datascience.codata.org/articles/10.5334/dsj-2020-043) (Collective Benefit, Authority to Control, Responsibility, and Ethics) are good starting point for thinking about data sovereignty and considering the ethics of data collected about an individual or groups of people.
1. Provide a "data dictionary" in your lesson, giving an overview of the data, where it came from, and how it was generated.
   Include a short description of each variable, a key for the column names in data tables, encoding of values, etc.
   For inspiration, see [the data dictionary from the Data Carpentry: Social Sciences curriculum](https://datacarpentry.org/socialsci-workshop/data.html).


#### Examples of Example Datasets

* The [Ecology Data Carpentry curriculum's](https://datacarpentry.org/lessons/#ecology) dataset comes from the [Portal
Project Teaching Database](https://figshare.com/articles/dataset/Portal_Project_Teaching_Database/1314459).
This dataset is an actual ecological research project's data that was simplified for teaching.
The reuse of this dataset throughout the Data Carpentry Ecology lessons helps stitch together the process of data analysis throughout the workshop, from data entry and cleaning to analysis and visualisation.
* The [Social Sciences Data Carpentry curriculum's](https://datacarpentry.org/lessons/#social-science) dataset is the 
[teaching version](https://figshare.com/articles/dataset/SAFI_Survey_Results/6262019) of the full Studying African Farmer-Led Irrigation (SAFI) dataset. 
The SAFI dataset represents interviews of farmers in Mozambique and Tanzania, conducted between November 2016 and June 2017.
The interviews surveyed household features (e.g. construction materials used for dwellings, number of household members), agricultural practices (e.g. water usage) and assets (e.g. number and types of livestock). 
The teaching version of the SAFI dataset has been simplified and intentionally "messed up"" to enable demonstrating common data cleaning issues often found in real-life data.
* [Patient inflammation dataset](https://swcarpentry.github.io/python-novice-inflammation/data/python-novice-inflammation-data.zip) - from the Software Carpentry Python [novice](https://swcarpentry.github.io/python-novice-inflammation/index.html) and the [incubating intermediate](https://carpentries-incubator.github.io/python-intermediate-development/index.html) lessons - is used to study the effect of a new treatment for arthritis by analysing the inflammation levels in patients who have been given this treatment.
* A [river catchment dataset](https://github.com/carpentries-incubator/python-intermediate-rivercatchment/tree/main/data) from the [Lowland Catchment Research (LOCAR) Datasets](https://catalogue.ceh.ac.uk/documents/db9f6ef9-9512-4f39-aca3-3c55f51a7487) is used in the [Earth and Environmental Sciences Intermediate Python lesson](https://carpentries-incubator.github.io/python-intermediate-development-earth-sciences/index.html) to analyse hydrological, hydrogeological, geomorphological and ecological interactions within permeable catchment systems. 
* Data Carpentry's [Astronomical Data Science with Python](https://datacarpentry.org/astronomy-python/) lesson uses two astronomical datasets, from the Gaia satellite and the Pan-STARRS photometric survey, to reproduce part of an analysis described in a published article.

#### Public Repositories for Data
The following repositories are good places to start looking for example data to use in your lesson, and/or to deposit the example data you produce.

- [Dryad](https://datadryad.org/)
- [The Open Science Framework](https://osf.io/)
- [The Offical Portal for European Data](https://data.europa.eu/)
- [Harvard Dataverse](https://dataverse.harvard.edu/)
- [DataONE](https://www.dataone.org/)
- [The Data Curation Network's datasets](https://datacurationnetwork.org/datasets/)
- [The Official Portal for Argentina Data](https://www.datos.gob.ar/) (in Spanish)
- [LANFRICA](https://lanfrica.com/)

GitHub is not a good place to store data, especially when it is large and/or does not consist of text files.
Instead, we recommend that you publish your example data elsewhere and link to it from your lesson website.
This has the added advantages that you can publish the data under its own license (ideally CC0, as discussed above), obtain a separate DOI for it, and create another backup of your data.
[Dryad](https://datadryad.org/), [Figshare](https://figshare.com/), the [Open Science Framework](https://osf.io/), and [Zenodo](https://zenodo.org/) are good general platforms for publishing data. 
However, if your lesson covers a particular domain with its own established standard for publishing data, we recommend that you use that.
The [Generalist Repositories Ecosystem Initiative (GREI)](https://datascience.nih.gov/data-ecosystem/generalist-repository-ecosystem-initiative) includes several more general options, and provides a [decision tree to help you choose the most appropriate location for your data](https://zenodo.org/records/11105430).

When you publish the data for your lesson, make sure to include:

* a description of each of the files included.
* information about the provenance of those files.
* the lesson in which those files are used.
* the license terms.
* anything else you think people need to know about the data.

See [the Figshare entry of data used in Data Carpentry Image Processing workshops](https://figshare.com/articles/dataset/Data_Carpentry_Image_Processing_Data_beta_/19260677) for an example.
