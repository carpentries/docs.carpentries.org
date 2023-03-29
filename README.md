# The Carpentries Handbook (BETA)

This is an early prototype of what The Carpentries Handbook might look like.  Everything is a work in progress and does not currently contain any actual Carpentries documentation.  The site can be [previewed at this Netlify link](https://carpentries-beta-handbook-preview.netlify.app/).

## File structure

* `/build/` Used to build local website. In `.gitignore` so this will not show up in the repo.  Do not edit these files.
* `/source/` Contains all the files needed to build the site.  Includes:
    * css files and page templates that override styles and templates in the theme
    * folders with `rst` files with content for each page. This includes one folder for each area of work, plus a folder called `pages` for general pages such as the style guide, glossary, and other landing pages.
    * `/_includes/` - text blocks and other content to be included in other pages
    * `/_templates/` - templates for specialized content such as the table of contents in the sidebar
    * `/_static/` - contains custom css styles 
    * `conf.py` - site settings
    * `index.rst` - sets structure for home page
* `.gitignore` Standard gitignore file
* `Makefile` - includes custom Make commands and inherits general Sphinx Make commands.

## Editing content

Content is organized in the `source` directory.  Edits to content should be made to these files.  Do not edit files in the `build` folder.

## Editing styles

Most styling comes from the `pydata_sphinx_theme` template.  Custom styles are implemented in `/source/_static/css`.  This includes the font files for the Mulish Google font and a custom css file.

## Editing templates and layouts

Most templates and layouts come from the `pydata_sphinx_theme` template.  Custom page templates are implemented in `/source/_templates/`.  For example, the standard theme includes Python functions to build templates for the table of contents in the sidebar and top navigation bar. Instead, we use custom and hard coded templates.  These are them called in `html_theme_options` in `conf.py`.

## Building the handbook

The handbook is built using Sphinx and the `pydata_sphinx_theme`.

* `make clean` Removes all files in the `build` directory
* `make html` Builds the site and publishes html content to the build directory

## Changes to `conf.py`

After setting the theme, the additional following changes were needed to `conf.py`.  Note this list does not include changes that only reflect The Carpentries identity (setting the name, social media handles, etc.).  The list includes changes that affect the site functionality.

* To make the template render markdown files properly, add `.md` to the `source_suffix` list and add `myst_parser` to the `extensions` list
* To use a custon style sheet, set `html_static_path = ['_static']` and `html_css_files = ['css/custom.css']`
* Add GitHub identifies to `html_context`. This is supposed to enable the "Edit on GitHub" button, but does not work.
* Add navbar and sidebar settings to `html_context`
* To use headers as anchor links, add `myst_heading_anchors = 6`
* To suppress warnings about duplicate headers across documents, add `suppress_warnings = ['autosectionlabel.*']`

## Previews on Netlify

This site is set up to preview all pull requests via [Netlify](https://app.netlify.com/sites/carpentries-beta-handbook-preview/overview). Note Netlify login is required to setup and manage Netlify.  All PRs will offer a public Netlify preview link.

## Useful links

* [Pydata Sphinx Theme](https://pydata-sphinx-theme.readthedocs.io/en/stable/index.html)
* [General Sphinx Documentation](https://www.sphinx-doc.org/en/master/usage/configuration.html#module-conf)
