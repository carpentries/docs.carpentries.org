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


# Get year for copyright
from datetime import date
current_year = str(date.today().year)

# -- Project information -----------------------------------------------------

project = 'The Carpentries Test Beta Handbook'
copyright = '{}, The Carpentries'.format(current_year)
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

# Needed to use headings as anchor links
# https://myst-parser.readthedocs.io/en/latest/syntax/optional.html#auto-generated-header-anchors
myst_heading_anchors = 6

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

html_context = {
    "default_mode": "light",
    "display_github": True, # Integrate GitHub
    "github_user": "carpentries", # Username
    "github_repo": "handbook-beta", # Repo name
    "github_version": "main", # Version
    "conf_py_path": "/source/", # Path in the checkout to the docs root    
    }

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


    # Set Carpentries title to show up at left section of top nav bar
    "navbar_start": ["navbar-logo"],

    # Set nothing e in center section of top nav bar
    "navbar_center": [],

    # Set where center area aligns to
    # https://pydata-sphinx-theme.readthedocs.io/en/v0.7.2/user_guide/configuring.html#configure-the-navbar-center-alignment
    "navbar_align": "content",

    # Set social media links right section of top nav bar
    "navbar_end": ["navbar-icon-links"],

    # Set nothing to always be in top nav bar, otherwise search is in nav bar
    "navbar_persistent": [],

    # Set what goes in secondary sidebar (right side)
    "secondary_sidebar_items": ["page-toc", "edit-this-page",],

    # Not actually needed when header menus are hard coded/custom built
    "header_links_before_dropdown": 0,

    # Do not show prev/next navigation at bottom, as handbooks are not sequential
    "show_prev_next": False
}


# Set what is displayed in main sidebar (left side)
# https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-html_sidebars
html_sidebars = {
    "**": ['globaltoc.html', 'search-field',  ]
}


# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
html_css_files = ['css/custom.css']

