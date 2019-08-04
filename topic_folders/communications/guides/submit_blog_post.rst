Collaborative Blog Post Writing
-------------------------------

The Carpentries welcomes blog posts from our community members including
workshop host sites, instructors, learners, and more. Are you interested
in publishing a post on The Carpentries blog?

Sharing blog post ideas
~~~~~~~~~~~~~~~~~~~~~~~

-  Join The Carpentries Slack and share your blog post idea in the
   #blog-post-ideas channel to start discussion and invite other
   community members to collaborate with you (preferred)

-  Email community[at]carpentries[dot]org with your idea and one of the
   team will facilitate amplification of the idea in the community so
   others can reach out and collaborate with you (option)

Sharing ready-to-publish drafts
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Our blog content is formatted in Markdown, and rendered as html thanks
to Jekyll. You can submit your blog post draft in one of three ways -
Email your blog post draft to community[at]carpentries[dot]org, or
submit it through `this
form <https://carpentries.typeform.com/to/BK55ld>`__ and one of the team
will follow up with you to get it published. (low time requirement)

If you wish to submit a blog post about your favourite tool or workflow,
you can submit the post through `this
form <https://docs.google.com/forms/d/e/1FAIpQLSeiu5NzJsLxYueaQrNn_qKbaa5JR2Sz12CeCRyedKQxwb54Dw/viewform>`__
and we will post it on the blog for you.

-  Create a HackMD file, convert your post to Markdown [`see Markdown
   cheatsheet <https://www.markdownguide.org/cheat-sheet/>`__], add a
   YAML header to the top of your Markdown file, open an issue in The
   Carpentries blog GitHub repository with new post appended to the
   issue title. One of the team will help get it published.
   (moderate-time requirement)

-  Convert your post to Markdown [`see Markdown
   cheatsheet <https://www.markdownguide.org/cheat-sheet/>`__], add a
   YAML header to the top of your Markdown file, and submit a Pull
   Request to The Carpentries blog GitHub repository (more tasking).

Read below and find out how to contribute a blog post to

-  `The Carpentries
   blog <#how-to-contribute-a-blog-post-to-the-carpentries-blog>`__
-  `Data Carpentry
   blog <#how-to-contribute-a-blog-post-to-data-carpentry>`__
-  `Library Carpentry
   blog <#how-to-contribute-a-blog-post-to-library-carpentry>`__
-  `Software Carpentry
   blog <#how-to-contribute-a-blog-post-to-software-carpentry>`__

How to Contribute a Blog Post to The Carpentries blog
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. If you wish to contribute a blog post, please work in
   https://github.com/carpentries/carpentries.org, which can be viewed
   at https://carpentries.org/blog/.

2. Posts go in the ``_posts`` folder.

3. Posts need to be created in
   `Markdown <https://guides.github.com/features/mastering-markdown/>`__
   and named according to this convention:

   ``YYYY-MM-DD-filename.md``

   e.g. 

   ``2018-04-29-book-review-teaching.md``

4. In order to render correctly, posts need to have a header block,
   which should be created like `this
   example <https://github.com/carpentries/carpentries.org/blob/gh-pages/_posts/2018/04/2018-04-25-website-launch.md>`__,
   e.g.

   ::

      ---
      layout: page
      authors: ["Tracy Teal", "Belinda Weaver"]
      teaser: "New website for access to all things Carpentries"
      title: "Launching The Carpentries Website"
      date: 2018-04-25
      time: "09:00:00"
      tags: ["Website", "Communications"]
      ---

   Separate the header block from the post text by inserting a new line.

5. All fields should be filled in. If there is more than one author,
   separate the author names like this: ``["Name 1", "Name 2"]``.

6. Images should be uploaded to the ``images`` folder. Images should be
   linked using Markdown, and paths to the image should be relative.

   Example:

   .. code:: md

      ![Image Description]({{ site.filesurl }}/images/myimage.jpg)

   A web link should be used for images hosted elsewhere. Please be sure
   you have rights to use this image before including it.

   Example:

   .. code:: md

      ![Image Description](https://web_address/pathway_to_full_image_filename)

   If you are not sure how to add images in Markdown format, look at an
   `existing post with a locally hosted
   image <https://github.com/datacarpentry/datacarpentry.github.io/blob/master/_posts/2017-12-19-frb_carpentry.md>`__
   and copy the formatting from there.

7. Once you have previewed your file, commit the Markdown file to your
   fork and start a Pull Request. We automatically run tests using
   `TravisCI <https://travis-ci.org/>`__ on your Pull Requests. Please
   review your pull request a few minutes after you’ve submitted it to
   make sure those tests have passed. These tests look for valid YAML
   headers and make sure that the post will build properly. Once tests
   have passed, Carpentries staff will review and merge your Pull
   Request or reach out to you with more questions.

How to Contribute a Blog Post to Data Carpentry
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. If you wish to contribute a blog post, please work in
   https://github.com/datacarpentry/datacarpentry.github.io, which can
   be viewed at http://www.datacarpentry.org/blog/.

2. Posts go in the ``_posts`` folder.

3. Posts need to be created in
   `Markdown <https://guides.github.com/features/mastering-markdown/>`__
   and named according to this convention:

   ``YYYY-MM-DD-filename.md``

   e.g. 

   ``2017-07-10-assess_report.md``

4. In order to render correctly, posts need to have a header block,
   which should be created like `this
   example <https://github.com/datacarpentry/datacarpentry.github.io/blob/master/_posts/2015-01-23-genomics-hackathon.md>`__,
   e.g.

   ::

      ---
      layout: post
      subheadline: "Lessons"
      title: Data Carpentry Genomics and Asssessment Hackathon
      teaser: "Announcing a Data Carpentry Genomics and Assessment Hackathon"
      header:
         image_fullwidth: "light-blue-wood-texture.jpg"
      categories:
         - blog
      comments: true
      show_meta: true
      authors: ["Tracy Teal", "Belinda Weaver"]
      ---

   Separate the header block from the post text by inserting a new line.

5. ``Subheadline`` is an optional field, as is ``teaser``, but the other
   fields should be filled in. If there is more than one author,
   separate the author names like this: ``["Name 1", "Name 2"]``.

6. Images should be uploaded to the ``images`` folder. Images should be
   linked using Markdown, and paths to the image should be relative.

   Example:

   .. code:: md

      ![Image Description]({{ site.filesurl }}/images/myimage.jpg)

   A web link should be used for images hosted elsewhere. Please be sure
   you have rights to use this image before including it.

   Example:

   .. code:: md

      ![Image Description](https://web_address/pathway_to_full_image_filename)

   If you are not sure how to add images in Markdown format, look at an
   `existing post with a locally hosted
   image <https://github.com/datacarpentry/datacarpentry.github.io/blob/master/_posts/2017-12-19-frb_carpentry.md>`__
   and copy the formatting from there.

7. Once you have previewed your file, commit the Markdown file to your
   fork and start a Pull Request. We automatically run tests using
   `TravisCI <https://travis-ci.org/>`__ on your Pull Requests. Please
   review your pull request a few minutes after you’ve submitted it to
   make sure those tests have passed. These tests look for valid YAML
   headers and make sure that the post will build properly. Once tests
   have passed, Carpentries staff will review and merge your Pull
   Request or reach out to you with more questions.

How to Contribute a Blog Post to Library Carpentry
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. If you wish to contribute a blog post, please work in
   https://github.com/LibraryCarpentry/librarycarpentry.github.io, which
   can be viewed at https://librarycarpentry.org.

2. Posts go in the ``_posts`` folder.

3. Posts need to be created in
   `Markdown <https://guides.github.com/features/mastering-markdown/>`__
   and named according to this convention:

   ``YYYY-MM-DD-filename.md``

   e.g. 

   ``2018-09-12-data-in-the-desert.md``

4. In order to render correctly, posts need to have a header block,
   which should be created like `this
   example <https://github.com/LibraryCarpentry/librarycarpentry.github.io/blob/master/_posts/2018/09/2018-09-12-data-in-the-desert.md>`__,
   e.g.

   ::

      ---
      layout: page
      authors: ["Tracy Teal", "Belinda Weaver"]
      title: "Data in the desert"
      teaser: "Library Carpentry workshop at the University of Arizona"
      date: 2018-09-12
      tags: ["University of Arizona", "Library Carpentry", "The Carpentries", "Workshop"]
      category: ["blog"]
      ---

   Separate the header block from the post text by inserting a new line.

5. All fields should be filled in. If there is more than one author,
   separate the author names like this: ``["Name 1", "Name 2"]``.

6. Images should be uploaded to the ``images`` folder. Images should be
   linked using Markdown, and paths to the image should be relative.

   Example:

   .. code:: md

      ![Image Description]({{ site.filesurl }}/images/myimage.jpg)

   A web link should be used for images hosted elsewhere. Please be sure
   you have rights to use this image before including it.

   Example:

   .. code:: md

      ![Image Description](https://web_address/pathway_to_full_image_filename)

   If you are not sure how to add images in Markdown format, look at an
   `existing post with a locally hosted
   image <https://github.com/LibraryCarpentry/librarycarpentry.github.io/blob/master/_posts/2018/09/2018-09-12-data-in-the-desert.md>`__
   and copy the formatting from there.

7. Once you have previewed your file, commit the Markdown file to your
   fork and start a Pull Request. We automatically run tests using
   `TravisCI <https://travis-ci.org/>`__ on your Pull Requests. Please
   review your pull request a few minutes after you’ve submitted it to
   make sure those tests have passed. These tests look for valid YAML
   headers and make sure that the post will build properly. Once tests
   have passed, Carpentries staff will review and merge your Pull
   Request or reach out to you with more questions.

Alternative Ways to Post
''''''''''''''''''''''''

If you are new to GitHub and want to submit a blog post without using
this workflow, you can submit it through `this
form <https://goo.gl/forms/xXDUwhq0rPY0jC5r2>`__ and we will post it to
the blog for you.

How to Contribute a Blog Post to Software Carpentry
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. If you wish to contribute a blog post, please work in
   https://github.com/swcarpentry/website, which can be viewed at
   https://software-carpentry.org/blog.

2. Posts go in the ``_posts`` folder, which is divided up first by year,
   e.g. \ ``2017``, and then by month, e.g. \ ``07``. Be sure to start
   creating your file in the correct folder.

3. Posts need to be created in
   `Markdown <https://guides.github.com/features/mastering-markdown/>`__
   and named according to this convention:

   ``YYYY-MM-DD-filename.md``

   e.g. 

   ``2017-07-10-assess_report.md``

4. In order to render correctly, posts need to have a header block,
   which should be created like `this
   example <https://github.com/swcarpentry/website/blob/gh-pages/_posts/2017/06/2017-06-19-mqu-ttt.md>`__,
   e.g.

   ::

      ---
      layout: post
      subheadline: "Assessment"
      title: "Analysis of Software Carpentry Workshop Impact"
      date: 2017-07-10
      time: "08:00:00"
      authors: ["Tracy Teal", "Belinda Weaver"]
      category: ["surveys", "workshops", "impact", "assessment"]
      ---

   Separate the header block from the post proper by a new line.

5. ``Subheadline`` is an optional field, as is ``time``, but the other
   fields should be filled in. If there is more than one author,
   separate the author names like this: ``["Name 1", "Name 2"]``.
   Separate any categories the same way.

6. Images should be uploaded to the appropriate year in the
   ``files/<year>/<month>`` folder. Images should be linked using
   Markdown, and paths to the image should be relative.

   Example:

   .. code:: md

      ![Image Description]({{ site.filesurl }}/2017/07/myimage.jpg)

   A web link should be used for images hosted elsewhere. Please be sure
   you have rights to use this image before including it.

   Example:

   .. code:: md

      ![Image Description](https://web_address/pathway_to_full_image_filename)

   If you are not sure how to add images in Markdown format, look at an
   `existing post with a locally hosted
   image <https://github.com/swcarpentry/website/blob/gh-pages/_posts/2017/06/2017-06-19-mqu-ttt.md>`__
   or `one with a web
   link <https://github.com/swcarpentry/website/blob/gh-pages/_posts/2017/07/2017-07-10-assess_report.md>`__
   and copy the formatting from there.

7. Once you have previewed your file, commit the Markdown file to your
   fork and start a Pull Request. We automatically run tests using
   `TravisCI <https://travis-ci.org/>`__ on your Pull Requests. Please
   review your pull request a few minutes after you’ve submitted it to
   make sure those tests have passed. These tests look for valid YAML
   headers and make sure that the post will build properly.

Troubleshooting
^^^^^^^^^^^^^^^

The most likely reason posts fail to build is because of ‘rogue’
characters in the YAML header. Rogue characters generally occur because
material has been pasted in directly from programs like Word or Google
documents. The most common rogue characters that cause issues are smart
quotes (curly quote marks as opposed to plain ones), but others might be
em or en dashes, mathematical or other symbols, or other characters that
cannot be rendered in plain text by typing on a keyboard. Replace smart
quotes with plain quote marks and smart em or en dashes with plain
hyphens to avert any problems.
