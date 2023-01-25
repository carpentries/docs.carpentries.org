# The Carpentries Handbook (BETA)

This is an early prototype of what The Carpentries Handbook might look like.  Everything is a work in progress and does not currently contain any actual Carpentries documentation.

## File structure

* `/build/` Used to build local website. In `.gitignore` so this will not show up in the repo.  Do not edit these files.
* `/docs/`  Used to build the github pages site.  It is not necessary to use this during local development. Do not edit these files.
* `/source/` Contains all the files needed to build the site.  Includes:
    * css files and page templates that override styles and templates in the theme
    * folders with markdown files with content for each page
    * `conf.py` - site settings
    * `index.rst` - sets structure for home page
* `.gitignore` Standard gitignore file
* `Makefile` - includes custom Make commands and inherits general Sphinx Make commands.

## Editing content

Content is organized in the `source` directory.  There is one folder for each team's work, with markdown files in each folder for each handbook.  Edits to content should be made to these files.  Do not edit files in the `build` or `docs` folders.

## Editing styles

Most styling comes from the `pydata_sphinx_theme` template.  Custom styles are implemented in `/source/_static/css`.  This includes the font files for the Mulish Google font and a custom css file.

## Editing templates and layouts

Most templates and layouts come from the `pydata_sphinx_theme` template.  Custom page templates are implemented in `/source/_templates/`.  For example, the standard theme includes Python functions to build templates for the table of contents in the sidebar and top navigation bar. Instead, we use custom and hard coded templates.  These are them called in `html_theme_options[navbar_center]` in `conf.py`. 

## Editing anchor links

An anchor link will link to another section of the page you are on (as opposed to going to a different page).  Anchor links can be derived from section header titles (beginning with 1-6 `#` signs in markdown).  The anchor link text is a single `#` sign followed by the section header text, in all lowercase, with spaces replaced by hyphens.

For example, this header:

```
## Welcome to The Carpentries
```

could be linked to in markdown as follows:

```
Read more by reviewing our [welcome page](#welcome-to-the-carpentries).
```

## Building the handbook

The handbook is built using Sphinx and the `pydata_sphinx_theme`.

* `make clean` Removes all files in the `build` directory
* `make html` Builds the site and publishes html content to the build directory
* `make github` Builds the site and publishes html content to the build directory. This also creates a copy in the docs directory, enabling the site to render at https://carpentries.github.io/handbook-beta/

Note `build` can be in `.gitignore` but `docs` should not be as long as we want this built directly from GitHub.  These settings may need to be changed once the site is ready to go live.

## Changes to `conf.py`

After setting the theme, the additional following changes were needed to `conf.py`.  Note this list does not include changes that only reflect The Carpentries identity (setting the name, social media handles, etc.).  The list includes changes that affect the site functionality.

* To make the template render markdown files properly, add `.md` to the `source_suffix` list and add `myst_parser` to the `extensions` list
* To use a custon style sheet, set `html_static_path = ['_static']` and `html_css_files = ['css/custom.css']`
* Add an empty `.nojekyll` file to the `docs` folder to enable the build on GitHub pages
* Add GitHub identifies to `html_context`. This is supposed to enable the "Edit on GitHub" button, but does not work.
* Add navbar and sidebar settings to `html_context`
* To use headers as anchor links, add `myst_heading_anchors = 6` to conf.py

## Previews on Netlify

This site is set up to preview all pull requests via [Netlify](https://app.netlify.com/sites/carpentries-beta-handbook-preview/overview). [Section needs updating.]
