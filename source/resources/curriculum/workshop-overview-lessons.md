# Curriculum Overview Pages
By default, The Carpentries Workbench is designed to build [lesson websites consisting of multiple episode pages](./curriculum-structure.md), reflecting the typical structure of our lessons.
However, it is sometimes helpful to be able to provide a single-page "lesson" site, typically as an overview or "landing page" for a collection of lessons that belong together ([we call this a _curriculum_](./curriculum-structure.md#curriculum)).

In the Workbench, this is supported with the optional `overview` parameter in the global configuration file (`config.yaml`).
Adding `overview: true` as a new line to `config.yaml` prevents the infrastructure from raising an error if no files are present in the `episodes` folder. The front page of the overview site is built from the `index.md` and `learners/setup.md` as usual.

## What should an overview page contain?
Lesson developers can choose to populate these pages however they like.
Here are some recommendations for what to include:

* A short description of the curriculum as a whole, including its target audience and most important learning outcomes.
* A list of prerequisite knowledge for the curriculum. (This can be formatted as a fenced div with the `prereq` class.)
* A table describing the lessons included in the curriculum, and the recommended order in which they should be taught.
	* If multiple possible pathways exist through your curriculum, these should be described as individual tables or in some introductory text before the table of all lessons is displayed. If many pathways exist through your lessons, describe these on a separate page built from a source file in the `learners/` folder and link to it from `index.md`.
* Setup instructions such as for software installation and data download should be described in `learners/setup.md`.
  As with a lesson in the default configuration, the contents of this page will be appended to the landing page of the site.
* If your lessons share a common example dataset, you may wish to describe it on a dedicated page in this overview site.
  For example, this page could include a _data dictionary_ describing the features of the dataset, a brief description of its origins, a link to the raw data, and a link to further information (e.g. a publication featuring the original data).
	* See the [_Workshop Data_ page of the Data Carpentry Ecology Curriculum Overview](https://datacarpentry.org/ecology-workshop/data.html) for an example.

All of the items described above should be included in the overview site of an official Carpentries curriculum.


## Template Markdown for Curriculum Overview Table
Make a copy of this template to help you build a Markdown table describing the lessons in your curriculum.


```markdown
| **Lesson**                                   | **Overview**                                                               |
|:-------------------------------------------- | -------------------------------------------------------------------------- |
| [Title of First Lesson](URL-of-lesson-site)  | A short description what the first lesson teaches                          |
| [Title of Second Lesson](URL-of-lesson-site) | A short description what the second lesson teaches                         | 
| ...                                          | Keep adding lines in this format until you have listed all of your lessons |
```
