### Submitting blog posts 

The Carpentries welcomes blog posts from our community members including workshop host sites, instructors, learners, and more.

#### How to Contribute a Blog Post to The Carpentries blog

1.  If you wish to contribute a blog post,
    please work in <https://github.com/carpentries/carpentries.org>,
    which can be viewed at <https://carpentries.org/blog/>.
    
1.  Posts go in the `_posts` folder. 
    
1.  Posts need to be created in [Markdown](https://guides.github.com/features/mastering-markdown/) and named 
    according to this convention:
    
    `YYYY-MM-DD-filename.md`
    
    e.g. 
    
    `2018-04-29-book-review-teaching.md`
    
1.  In order to render correctly, posts need to have a header block, which should be created like [this example](https://raw.githubusercontent.com/carpentries/carpentries.org/gh-pages/_posts/2018/04/2018-04-25-website-launch.md), e.g.

    ```
    ---
    layout: page
    authors: ["Tracy Teal", "Belinda Weaver"]
    teaser: "New website for access to all things Carpentries"
    title: "Launching The Carpentries Website"
    date: 2018-04-25
    time: "09:00:00"
    category: [ "Website"]
    ---
    ```

    Separate the header block from the post text by inserting a new line. 
    
1.  All fields should be filled in. If there is more than one author, separate the author names like this: `["Name 1", "Name 2"]`. 
    
1.  Images should be uploaded to the `images` folder. Images should be linked using Markdown, and paths to the image should be relative. 
    
    Example: 
    ```md
    ![Image Description]({{ site.filesurl }}/images/myimage.jpg)
    ```
    A web link should be used for images hosted elsewhere. Please be sure you have rights to use this image before including it.

    Example: 
    ```md
    ![Image Description](https://web_address/pathway_to_full_image_filename)
    ```
    
    If you are not sure how to add images in Markdown format, look at an [existing post with a locally hosted image](https://raw.githubusercontent.com/datacarpentry/datacarpentry.github.io/master/_posts/2017-12-19-frb_carpentry.md) and copy the formatting from there.
    
1. Once you have previewed your file, commit the Markdown file to your fork and start a Pull Request. We automatically run tests using [TravisCI](https://travis-ci.org/) on your Pull Requests. Please review your pull request a few minutes after you've submitted it to make sure those tests have passed. These tests look for valid YAML headers and make sure that the post will build properly. Once tests have passed, Carpentries staff will review and merge your Pull Request or reach out to you with more questions.

##### Alternative Ways to Post
If you are new to GitHub and want to submit a blog post without using this workflow, you can submit it through [this form](https://carpentries.typeform.com/to/BK55ld) and we will post it to the blog for you.

If you wish to submit a blog post about a favourite tool or research workflow, you can submit the post through [this form](https://docs.google.com/forms/d/e/1FAIpQLSeiu5NzJsLxYueaQrNn_qKbaa5JR2Sz12CeCRyedKQxwb54Dw/viewform) and we will post it on the blog for you. 

#### How to Contribute a Blog Post to Data Carpentry

1.  If you wish to contribute a blog post,
    please work in <https://github.com/datacarpentry/datacarpentry.github.io>,
    which can be viewed at <http://www.datacarpentry.org/blog/>.
    
1.  Posts go in the `_posts` folder. 
    
1.  Posts need to be created in [Markdown](https://guides.github.com/features/mastering-markdown/) and named 
    according to this convention:
    
    `YYYY-MM-DD-filename.md`
    
    e.g. 
    
    `2017-07-10-assess_report.md`
    
1.  In order to render correctly, posts need to have a header block, which should be created like [this example](https://raw.githubusercontent.com/datacarpentry/datacarpentry.github.io/master/_posts/2015-01-23-genomics-hackathon.md), e.g.

    ```
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
    authors: ["Tracy Teal"]
    ---
    ```

    Separate the header block from the post text by inserting a new line. 
    
1.  `Subheadline` is an optional field, as is `teaser`, but the other fields should be filled in. If there is more than one author, separate the author names like this: `["Name 1", "Name 2"]`. 
    
1.  Images should be uploaded to the `images` folder. Images should be linked using Markdown, and paths to the image should be relative. 
    
    Example: 
    ```md
    ![Image Description]({{ site.filesurl }}/images/myimage.jpg)
    ```
    A web link should be used for images hosted elsewhere. Please be sure you have rights to use this image before including it.

    Example: 
    ```md
    ![Image Description](https://web_address/pathway_to_full_image_filename)
    ```
    
    If you are not sure how to add images in Markdown format, look at an [existing post with a locally hosted image](https://raw.githubusercontent.com/datacarpentry/datacarpentry.github.io/master/_posts/2017-12-19-frb_carpentry.md) and copy the formatting from there.
    
1. Once you have previewed your file, commit the Markdown file to your fork and start a Pull Request. We automatically run tests using [TravisCI](https://travis-ci.org/) on your Pull Requests. Please review your pull request a few minutes after you've submitted it to make sure those tests have passed. These tests look for valid YAML headers and make sure that the post will build properly. Once tests have passed, Carpentries staff will review and merge your Pull Request or reach out to you with more questions.

##### Alternative Ways to Post
If you are new to GitHub and want to submit a blog post without using this workflow, you can submit it through [this form](https://carpentries.typeform.com/to/BK55ld) and we will post it to the blog for you.

If you wish to submit a blog post about a favourite tool or research workflow, you can submit the post through [this form](https://docs.google.com/forms/d/e/1FAIpQLSeiu5NzJsLxYueaQrNn_qKbaa5JR2Sz12CeCRyedKQxwb54Dw/viewform) and we will post it on the blog for you. 


#### How to Contribute a Blog Post to Software Carpentry

1.  If you wish to contribute a blog post,
    please work in <https://github.com/swcarpentry/website>,
    which can be viewed at <https://software-carpentry.org/blog>.
    
1.  Posts go in the `_posts` folder, which is divided up first by year,  e.g. `2017`, and then by month, e.g. `07`. Be sure to start creating your file in the correct folder. 
    
1.  Posts need to be created in [Markdown](https://guides.github.com/features/mastering-markdown/) and named according to this convention:
    
    `YYYY-MM-DD-filename.md`
    
    e.g. 
    
    `2017-07-10-assess_report.md`
    
1.  In order to render correctly, posts need to have a header block, which should be created like [this example](https://raw.githubusercontent.com/swcarpentry/website/gh-pages/_posts/2017/06/2017-06-19-mqu-ttt.md), e.g.

    ```
    ---
    layout: post
    subheadline: "Assessment"
    title: "Analysis of Software Carpentry Workshop Impact"
    date: 2017-07-10
    time: "08:00:00"
    authors: ["Kari L. Jordan"]
    category: ["surveys", "workshops", "impact", "assessment"]
    ---
    ```

    Separate the header block from the post proper by a new line. 
    
1.  `Subheadline` is an optional field, as is `time`, but the other fields should be filled in. If there is more than one author, separate the author names like this: `["Name 1", "Name 2"]`. Separate any categories the same way.
    
1.  Images should be uploaded to the appropriate year in the `files/<year>/<month>` folder. Images should be linked using Markdown, and paths to the image should be relative. 
    
    Example: 
    
    ```md
    ![Image Description]({{ site.filesurl }}/2017/07/myimage.jpg)
    ```
    
    A web link should be used for images hosted elsewhere. Please be sure you have rights to use this image before including it.

    Example: 
    
    ```md
    ![Image Description](https://web_address/pathway_to_full_image_filename)
    ```
    
    If you are not sure how to add images in Markdown format, look at an [existing post with a locally hosted image](https://raw.githubusercontent.com/swcarpentry/website/gh-pages/_posts/2017/06/2017-06-19-mqu-ttt.md) or [one with a web link](https://raw.githubusercontent.com/swcarpentry/website/gh-pages/_posts/2017/07/2017-07-10-assess_report.md) and copy the formatting from there.
    
7.  Once you have previewed your file, commit the Markdown file to your fork and start a Pull Request. We automatically run tests using [TravisCI](https://travis-ci.org/) on your Pull Requests. Please review your pull request a few minutes after you've submitted it to make sure those tests have passed. These tests look for valid YAML headers and make sure that the post will build properly.

##### Alternative Ways to Post
If you are new to GitHub and want to submit a general blog post without using this workflow, you can submit it through [this form](https://carpentries.typeform.com/to/BK55ld) and we will post it to the blog for you.

If you wish to submit a blog post specifically about a favourite tool or research workflow, you can submit the post through [this form](https://docs.google.com/forms/d/e/1FAIpQLSeiu5NzJsLxYueaQrNn_qKbaa5JR2Sz12CeCRyedKQxwb54Dw/viewform) and we will post it on the blog for you. 

#### Troubleshooting

The most likely reason posts fail to build is because of 'rogue' characters in the YAML header. Rogue characters generally occur because material has been pasted in directly from programs like Word or Google documents. The most common rogue characters that cause issues are smart quotes (curly quote marks as opposed to plain ones), but others might be em or en dashes, mathematical or other symbols, or other characters that cannot be rendered in plain text by typing on a keyboard. Replace smart quotes with plain quote marks and smart em or en dashes with plain hyphens to avert any problems.

