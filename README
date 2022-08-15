# The Carpentries Handbook (BETA)

This is an early prototype of what The Carpentries Handbook might look like.  Everything is a work in progress and does not currently contain any actual Carpentries documentation.

## Building the handbook

The handbook is built using Sphinx and the `pydata_sphinx_theme`.

* `make clean` Removes all files in the `build` directory
* `make html` Builds the site and publishes html content to the build directory
* `make github` Builds the site and publishes html content to the build directory. This also creates a copy in the docs directory, enabling the site to render at https://carpentries.github.io/handbook-beta/

Note `build` can be in `.gitignore` but `docs` should not be as long as we want this built directly from GitHub.

## Changes to `conf.py`

After setting the theme, the additional following changes were needed to `conf.py`:

* To make the template render markdown files properly, add `.md` to the `source_suffix` list and add `myst_parser` to the `extensions` list
* To use a custon style sheet, set `html_static_path = ['_static']` and `html_css_files = ['css/custom.css']`
* Add an empty `.nojekyll` file to the `docs` folder to enable the build on GitHub pages

