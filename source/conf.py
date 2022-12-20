# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'The Carpentries Test Beta Handbook'
copyright = '2022, The Carpentries'
author = 'The Carpentries'

# The full version, including alpha/beta/rc tags
release = '0.0.1'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'myst_parser'
]

# The suffix of source filenames.
source_suffix = [".rst", ".md"]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'pydata_sphinx_theme'

html_context = {"default_mode": "light"}

html_title = "The Carpentries Handbook"

html_theme_options = {
        "icon_links": [
        {
            "name": "GitHub",
            "url": "https://github.com/carpentries/",
            "icon": "fab fa-github-square",
            "type": "fontawesome",
        },
        {
            "name": "Mastodon",
            "url": "https://fosstodon.org/@thecarpentries",
            "icon": "fab fa-mastodon",
            "type": "fontawesome",
        },
        {
            "name": "Twitter",
            "url": "https://twitter.com/thecarpentries",
            "icon": "fab fa-twitter-square",
            # The default for `type` is `fontawesome` so it is not actually required in any of the above examples as it is shown here
        },
    ],
    
"navbar_start": ["navbar-logo"],
"navbar_center": ["navbar-handbooks", "navbar-general", "navbar-icon-links"],
"navbar_end": [],
"navbar_persistent": [],
     "secondary_sidebar_items": ["page-toc", "edit-this-page",],

     "header_links_before_dropdown": 0,
     "navbar_align": "content"


}


# https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-html_sidebars
html_sidebars = {
    "**": ['globaltoc.html', 'search-field',  ]
}


# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
html_css_files = ['css/custom.css']

