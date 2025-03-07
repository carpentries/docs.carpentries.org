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

project = 'The Carpentries Handbook'
copyright = '{}, The Carpentries'.format(current_year)
author = 'The Carpentries'

# The full version, including alpha/beta/rc tags
release = '0.0.1'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'myst_parser',
    'sphinx.ext.autosectionlabel',
    'sphinx.ext.extlinks',
    'sphinx_design',
    'notfound.extension',
]

notfound_urls_prefix = ""

myst_enable_extensions = ["colon_fence",
                          "substitution",
                          "deflist",
                          "attrs_block",]

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
html_favicon = "img/logo.ico"

html_context = {
    "default_mode": "light",
    "display_github": True, # Integrate GitHub
    "github_user": "carpentries", # Username
    "github_repo": "docs.carpentries.org", # Repo name
    "github_version": "main", # Version
    "doc_path": "source",
    "conf_py_path": "/source/", # Path in the checkout to the docs root
    "edit_page_url_template": "{{gh_repo}}{{file_name}}",
    "gh_repo":"https://github.com/carpentries/docs.carpentries.org/blob/main/source/"
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
            "url": "https://hachyderm.io/@thecarpentries",
            "icon": "fab fa-mastodon",
            "type": "fontawesome",
        },

        {
            "name": "Zenodo",
            "url": "https://zenodo.org/communities/carpentries/records",
            "icon": "_static/zenodo-logo.svg",
            "type": "local"
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

    # Set what goers in the footer
    "footer_start": ["footer_start.html",],

    # "footer_end": ["copyright.html","theme-version.html", "sphinx-version.html",],
    "footer_end": ["footer_end.html"],


    # Not actually needed when header menus are hard coded/custom built
    "header_links_before_dropdown": 0,

    # Do not show prev/next navigation at bottom, as handbooks are not sequential
    "show_prev_next": False,

    # Show the "edit on github" button
    # See https://pydata-sphinx-theme.readthedocs.io/en/stable/user_guide/source-buttons.html#add-an-edit-button
    "use_edit_page_button": True,


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

suppress_warnings = ['autosectionlabel.*']

# These links can be used anywhere in this documentation.

handbook_url = "https://docs.carpentries.org/"

myst_substitutions = {
  # AMY links
  "amy_link": "https://amy.carpentries.org",
  "amy_docs": "https://carpentries.github.io/amy/users_guide/community_index/",

  # Communications
  "slack": "https://carpentries.slack.com",
  "slack_invite": "https://slack-invite.carpentries.org/",
  "topicbox": "https://carpentries.topicbox.com/groups",
  "etherpad": "https://pad.carpentries.org",
  "codimd": "https://codimd.carpentries.org",

  # GitHub repos
  "gh_repo": "https://github.com/carpentries/docs.carpentries.org",

  # Curricula
  "instructor_training_curriculum":"https://carpentries.github.io/instructor-training/",
  "maintainer_onboarding": "https://carpentries.github.io/maintainer-onboarding/",
  "lesson_development_training": "https://carpentries.github.io/lesson-development-training",

  # General resources
  "glossary": "https://github.com/carpentries/community-engagement/blob/main/glossary.md",
  "code_of_conduct": handbook_url + "policies/coc/",
  "donate": "https://www.zeffy.com/en-US/donation-form/donate-to-make-a-difference-7497",
  "topicbox_guide": "https://docs.google.com/document/d/1lk1KmImG-5nkYzukjFMZMTS4BEVaOkqBg5_V_aj85_U/",
  "slack_guide": "https://docs.google.com/document/d/1-NcL-ofnHXjJnopdWH6jLrdLHhDJeZO3/",

  # Websites
  "carpentries_website": "https://carpentries.org",
  "handbook_url": handbook_url,

  # Email contacts
  "team_email": "team@carpentries.org",
  "instructor_training_email": "instructor.training@carpentries.org",
  "workshops_email": "workshops@carpentries.org",
  "membership_email": "membership@carpentries.org",
  "community_email": "community@carpentries.org",
  "curriculum_email": "curriculum@carpentries.org",

}
