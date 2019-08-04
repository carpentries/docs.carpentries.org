Why was this handbook created?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Historically, information and resources related to `The
Carpentries <https://carpentries.org/>`__ have been spread across
various websites, Google docs, GitHub repos, and more. The handbook is a
one-stop shop that consolidates information on running a workshop,
developing or maintaining lessons, participating in an instructor
training event, and more!

Many community members have contributed to this handbook, and we welcome
feedback on this Handbook. Feel free to submit issues or pull requests
to `this GitHub repo <https://github.com/carpentries/handbook/>`__ to
improve this community resource.

Building this site
~~~~~~~~~~~~~~~~~~

This site is built using the
`Sphinx <http://www.sphinx-doc.org/en/stable/>`__ documentation
generator (a Python tool) and the `Read the Docs
theme <https://github.com/rtfd/sphinx_rtd_theme>`__ for the style. (Not
to be confused with readthedocs.io - the site is *not* hosted at
readthedocs.io!)

For more information about using Sphinx, see the `Getting Started guide
(sphinx-doc.org) <http://www.sphinx-doc.org/en/stable/usage/quickstart.html>`__
or the `Quick Start
(readthedocs.io) <https://docs.readthedocs.io/en/latest/intro/getting-started-with-sphinx.html#quick-start>`__
for an explanation of how to use Sphinx.

Required dependencies
^^^^^^^^^^^^^^^^^^^^^

To install the required dependencies (Sphinx and the ReadTheDocs Sphinx
theme), execute the following command from the repository directory to
install all Python dependencies:

::

   pip install -r requirements.txt 

After installing the dependencies, you can build the site locally by
executing the following command from the repository:

::

   $ make html

Open the file ``_build/html/index.html`` to preview the site locally.
Python offers a quick way to run a web server to serve local files. Run
the following:

::

   $ cd _build/html

   # Python 2:
   $ python2 -m SimpleHTTPServer

   # Python 3:
   $ python3 -m http.server

In both cases, a local web server will be run on port ``8000``, so
navigate to http://localhost:8000 in your browser to view the site
locally.

You can make changes to the contents of the repository, and re-run
``make html``, to update the website contents. If you are having
problems with the site not refreshing, you can delete the contents of
the ``_build`` directory (which are automatically generated) with
``rm -fr _build/*``.

If new files or folders are added to the Handbook, ``index.rst`` will
need to be updated for those to be included in the final site by Sphinx.

Site structure
^^^^^^^^^^^^^^

The root level ``index.rst`` generates the main categories and the
sidebar navigation. Each sub-section is a folder in the
``topic_folders`` directory. Each folder within the ``topic_folders``
directory has its own ``index.rst`` file. These then expand into the
subcategories in each directory.

Within each folder’s ``index.rst`` file, the section heading is defined
by a string of ``=`` beneath it. Subheadings can be defined using
``###`` in each markdown file or by a heading with ``-`` under it in the
``index.rst`` file.

Formatting Hyperlinks
'''''''''''''''''''''

In markdown documents, links can be formatted in standard markdown, with
the text in square brackets and the hyperlink in parentheses:

::

   [text](hyperlink)

For the ``index.rst`` files, links must be formatted as follows. Note
the text is followed by the hyperlink in pointy brackets, everything is
wrapped in backticks, and then followed by an underscore.

::

   `text<hyperlink>`_

**Links to external markdown documents**

Something in this template causes ``.md`` extensions to get stripped,
breaking links to things like markdown documents in a GitHub repo. This
can be fixed by adding an anchor tag (``#``) to the end of the url. For
example,
``https://github.com/carpentries/handbook/blob/topic_folders/file.md``
would become
``https://github.com/carpentries/handbook/blob/topic_folders/file.md#``.

Additional information
^^^^^^^^^^^^^^^^^^^^^^

This site is built from the master branch of `this repo
(carpentries/handbook) <https://github.com/carpentries/handbook/>`__.
Changes can be previewed live here: http://docs-src.carpentries.org/.
Changes to the actual site https://docs.carpentries.org/ can take up to
a day to go live once changes have been pushed to GitHub, since the
contents of the site are behind a CDN (Content Distribution Network)
that caches content.

If you are making experimental changes to content please be sure to do
so in a non-master, non-live branch. When your changes are complete and
ready to be pushed to the live site, open a pull request in
`carpentries/handbook <https://github.com/carpentries/handbook>`__.

Draft content can be added to the `drafts folder of the
carpentries/userguides
repo <https://github.com/carpentries/usersguides/tree/master/drafts>`__
(in the master branch) without breaking anything. Draft content is not
built to the live site and these files may contain inaccurate or out of
date information.
