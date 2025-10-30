# Lesson Developers Handbook

## About This Handbook 

The Lesson Developers Handbook is designed to support members of The
Carpentries community who are serving as a Lesson Developer. It is maintained by The Carpentries Curriculum Team.  If you believe anything needs to be added or updated here, or if you would like to provide feedback on the content, please email the {{'[Curriculum Team](mailto:{})'.format(curriculum_email)}} or open an issue on the {{'[source repository of this handbook]({})'.format(gh_repo)}}. If you are unfamiliar with any of the terms used in this handbook, please refer to our {{'[Glossary of terms]({})'.format(glossary)}}.

## Roles and Responsibilities

Beyond ensuring that the lesson remains compliant with the requirements
for inclusion in [The Carpentries
Incubator](https://github.com/carpentries-incubator/proposals/blob/main/README.md#what-are-the-requirements-for-being-included-in-the-carpentries-incubator),
there are no formal responsibilities associated with developing a lesson
there: lesson projects in the Incubator are community efforts that
belong to the individual developers contributing to them. These
Developers can choose to manage them and commit time to them according
to their preferences and availability.

To ensure the continuing health and sustainability of their lesson
project, The Carpentries recommends that Lesson Developers make
themselves responsible for the following tasks:

-  Managing the design and development of the lesson.
-  Reading, responding to, and (where necessary) handling issues
   reported by community members.
-  Welcoming and reviewing pull requests and other contributions made by
   community members.
-  Communicating with the community about the ongoing development of the
   lesson.
-  Recruiting Instructors to beta test the lesson, supporting
   preparations for pilot workshops, and incorporating feedback from
   those workshops.
-  Submitting the lesson for open peer review and acceptance to [The
   Carpentries Lab](https://carpentries-lab.org).

## Onboarding

Lesson Developers can start a new lesson any time by opening a new
issue on [The Carpentries Incubator Proposals
repository](https://github.com/carpentries-incubator/proposals/issues/new?assignees=&labels=&template=issue_proposal.md).
The issue template includes several questions, which should be answered
to help the Curriculum Team set up the lesson repository correctly in
the Incubator.

Community members with an idea for a new lesson can also apply to join
Collaborative Lesson Development Training, which will be scheduled
periodically starting in 2023.

## Offboarding

There is no formal offboarding process for Lesson Developers working on
projects in The Carpentries Incubator.

To ensure the continuing health and sustainability of the project, The
Carpentries recommends that Lesson Developers take the following actions
when stepping away from a lesson:

-  Communicate the decision to the other developers of the lesson, so
   that they can redistribute tasks and plan the project accordingly.
-  Re-assign any issues assigned to them, to another member of the
   lesson development team.
-  Remove their name from the lesson README file and anywhere else where
   authors of the lesson are listed.
-  Ask the project owner (a developer with Admin access to the
   repository) to revoke the outgoing developer’s privileges on the
   lesson repository.
-  If the sole remaining developer of the lesson is leaving the project,
   add a notice to the top of the repository README and the lesson front
   page (`index.md`) to inform visitors that the lesson is not being
   actively maintained/developed. In these circumstances, consider:

   1. contacting the [Incubator administratorteam](mailto:incubator@carpentries.org) to let them know that the lesson will be unmaintained, and
   2. archiving the lesson repository.

If the developers wish to remove the lesson from The Carpentries
Incubator, the project owner (a developer with Admin access) can
transfer the lesson repository out of the `carpentries-incubator`
GitHub organisation via **Settings**->\ **General**->\ **Danger
Zone**->\ **Transfer Ownership**.

## Communication and Collaboration Spaces

### Community Calendar

Once scheduled, all Lesson Development Coworking Sessions are listed on
our [Community
Calendar](https://carpentries.org/community/#community-events). You
can add relevant events to your personal calendar from there by clicking
on the event you would like to attend.

### Etherpad

The Carpentries uses [Etherpad](/resources/communications/etherpads.md) as a collaborative note-taking tool during workshops, training, and other Carpentries-related events. Below is a list of Etherpads relevant to serving as a Lesson Developer.

-  [Pad-of-pads](https://pad.carpentries.org/pad-of-pads): A list of
   our most commonly used Etherpads and other resources.
-  [Lesson Development Coworking Session
   Notes](https://codimd.carpentries.org/lessondev-coworking): Signup
   information, connection details, and notes taken from monthly
   coworking sessions (CodiMD),

### GitHub

-  [The Carpentries Incubator Proposals
   repository](https://github.com/carpentries-incubator/proposals): a
   place for The Carpentries community to propose new lessons for
   development in the Incubator.
-  [The Carpentries Lab Reviews
   repository](https://github.com/carpentries-lab/reviews): a place
   for Lesson Developers to submit lessons for open peer review and
   acceptance to The Carpentries Lab.

### Slack

{{'[Join The Carpentries Slack workspace]({})'.format(slack_invite)}}. To follow conversations relevant to this role, you should join the following channels:

-  The #lesson-dev channel on The Carpentries Slack workspace is a platform for the whole community to ask questions and engage in discussions around the subject of lesson development.
-  We recommend that Lesson Developers browse existing channels in the 
   Slack workspace, for any that are relevant to the topic/domain of
   their lesson.
-  It can also be helpful to create a new channel for your lesson, as a
   space for you to discuss the development process with collaborators,
   and for community members to ask questions about the lesson.

If Slack is new to you, our {{"[Slack Guide]({})".format(slack_guide)}} will help you to set up your profile and give you an overview of how we use the platform on a day-to-day basis.

### Mailing List

You can access The Carpentries mailing lists from
[TopicBox](https://carpentries.topicbox.com/latest). The
[incubator-developers mailing list](https://carpentries.topicbox.com/groups/incubator-developers)
is the one relevant to serving in this role.

To join one or more Carpentries mailing lists, you will need to [create a login on the site](https://carpentries.topicbox.com/latest). Once you have done this, you can scroll through the list of groups and click “Join the Conversation” (for open mailing) or “Request to Join” (for those mailing lists requiring administrator approval). If you are new to Topicbox, please check out our {{"[Topicbox Guide]({})".format(topicbox_guide)}}.

## Step-by-Step Guides

### Using Issue Labels to Promote Collaboration

GitHub allows the maintainers of a repository to add contextual
information to Issues and Pull Requests in the form of labels. 
[The Carpentries uses an extended set of issue labels on its lesson repositories](../resources/curriculum/issue-labels.md).

Two labels, used by The Carpentries and in many repositories across GitHub,
can be deployed to increase the visibility of your lesson and encourage
community members to contribute to its development.

The **“help wanted”** label should be used to highlight issues with
which you would welcome additional help. The Carpentries website
includes a [Help Wanted
page](https://carpentries.org/help-wanted-issues/), which can
automatically list every issue labelled “help wanted” on repositories
from The Carpentries, Software Carpentry, Data Carpentry, Library
Carpentry, CarpentriesLab, and The Carpentries Incubator. Find out how
to include issues from your lesson repository on the Help Wanted page by
reviewing the [Information for
Maintainers](https://carpentries.org/help-wanted-issues/#for-maintainers)
on the page itself.

The **“good first issue”** label should be used to identify issues that
would make a good entry point for newcomers searching for a way to
contribute to your lesson. The work needed to close an issue with this
label would typically not require an extensive knowledge of the
structure or intricacies of your lesson repository, or an expert
understanding of the content. The “good first issue” label is used so
extensively that GitHub provides a page at\ `[repository
URL]/contribute <https://github.com/swcarpentry/r-novice-gapminder/contribute>`__
for every repository, listing issues with this label.

### Adding Topic Tags to a Lesson Repository

{{'[Official Lessons in The Carpentries Lesson Programs]({}/lessons/)'.format(carpentries_website)}} are listed on The Carpentries website, based on metadata describing the lesson. This metadata is added in the form of topic tags on the lesson repository. These topic tags should be set as soon as possible after the lesson has been created or added to the Incubator. Some are essential and taken from a limited set of values, while others are more flexible. The table below has guidance about the types and number of topic tags each lesson repository should have.


| Category   | Example            | Number | Description        |
|------------|-------------------|--------|--------------------|
| Lesson     | lesson             | 1      | Must be lesson to be listed on the Community Developed Lessons page     |
| Location   | data-carpentry     | 1      | A description of what lesson program the lesson belongs to with words separated by hyphens (i.e software-carpentry, data-carpentry, and library-carpentry) |
| Language   | español            | >0     | The language(s) the lesson is available in |
| Stage      | stable             | 1      | The current development stage for the lesson |
| Domain     | microbial-ecology  | 1-2    | The high-level domain(s) of the lesson for a general categorization |
| Tools      | python             | 1-3    | The main tool(s) taught in the lesson   |
| Skills     | taxonomic-classification | 1-3    | The main skill(s) taught in the lesson    |


The Curriculum Team will support you in setting appropriate topic tags
for your lesson. To help ensure consistency across all lesson
repositories developed by The Carpentries community, please refer
to [this listing](https://docs.google.com/spreadsheets/d/1KkmBtCu4PaNb5nzJAD82UHcfHQlaPY84qPVxw8WO8es/edit?usp=sharing)
of topic tags currently in use in The Carpentries Incubator, and re-use
these values where appropriate, creating new topic tags where no
pre-existing label exists for your lesson.


### [How to Organise a Lesson Development Sprint](/resources/curriculum/lesson-sprint-recommendations.md)

Many Lesson Developers find it helpful to organise a dedicated event to make progress and enhance collaboration on their lesson projects. 
This resource provides a set of recommendations for how to organise an effective and inclusive lesson development sprint event.

### Promoting Your Project in The Incubator Lesson Spotlight

The Incubator Lesson Spotlight is a regular feature in The Carpentries
blog and newsletter, highlighting a lesson currently under community
development. The purpose of the Spotlight series is to raise the
visibility of that lesson among the broader community, and to encourage
community members to contribute to the further development of that
lesson.

Any lesson in [The Carpentries
Incubator](https://github.com/carpentries-incubator/) is eligible to
be included in the series, regardless of the stage of development that
lesson is currently in. It is a good way for lessons in the early stages
of development to attract new collaborators, and for those in later
stages to invite others to informally review the lesson and to try
teaching the material. To submit your lesson to be featured in the
series, follow the steps below.

1. Think about how you can prepare your lesson for new contributors
   before the feature is published. This might mean labelling existing
   issues (e.g. to appear on [the Help Wanted
   page](https://carpentries.org/help-wanted-issues/)) or creating
   new ones, making sure that your CONTRIBUTING.md is up-to-date, and/or
   planning publication of the Spotlight feature to fit with a
   relatively quiet period in your schedule so that you can respond
   promptly to any new issues and pull requests.
2. Fill in the [Incubator Lesson Spotlight content submission
   form](https://docs.google.com/forms/d/e/1FAIpQLScJimGMtzqAFE-Tii-LvbfGZqtKj0OC4ken7_Qdlta8uZXAUA/viewform),
   providing details of the lesson to be included in the feature. It may
   be beneficial to collaborate on this content with other developers
   working on the lesson. The Carpentries Core Team will use the content
   provided in the form to create a post for [The Carpentries
   blog](https://carpentries.org/blog/) and an item for
   the [Carpentries Clippings newsletter](https://carpentries.org/newsletter/).
3. When the blog post has been drafted, a pull request will be opened to
   add that post to the website. You will be tagged for an (optional)
   review of this pull request before it is published. To review the
   blog post, read through the post content and comment on the issue
   thread to request any changes to the feature.

### Submitting a Lesson to The Carpentries Lab

The Carpentries Lab hosts community-developed lessons that have been
peer reviewed and can be relied upon by Instructors to meet a high
standard of quality and stability. The Lab provides a platform for open
peer review of lessons, and to promote the lessons that have entered the
collection.

To submit a lesson for peer review in The Carpentries Lab, follow these
steps:

1. Check the [eligibility criteria for lessons to be reviewed in the
   Lab](https://github.com/carpentries-lab/reviews#what-makes-a-lesson-a-good-candidate-for-the-carpentries-lab).
2. Open a new issue on the [Reviews
   repository](https://github.com/carpentries-lab/reviews/issues/new?assignees=&labels=new-submission&template=submission.md&title=%5BREV%5D%3A+)
   and answer the questions in the issue template to tell the Editors
   about the lesson.

### [Piloting a Lesson](/resources/curriculum/lesson-pilots.md)

Teaching a lesson for the first time is very rewarding, but the experience of the Instructors and learners also identifies opportunities to address and further clarify parts of the content. 
This makes early lesson teachings, which we refer to as *lesson pilots*, crucial milestones in the development of a high-quality lesson. 
This resource provides more information about how to test a new lesson in workshops, how these pilot workshops align with [the Lesson Life Cycle](/resources/curriculum/lesson-life-cycle.md), and guidance on logistics, gathering relevant feedback, etc.

## Resources


### [Introduction to The Carpentries Workbench](https://carpentries.github.io/sandpaper-docs/)

Documentation for The Carpentries Workbench, open source infrastructure
for lesson websites. The documentation explains how to install the
Workbench so that Lesson Developers can edit and preview their lessons
on their own computer, how to initialise a new lesson and use the
various elements of the lesson template, and how to keep up to date with
the latest changes to the infrastructure.

### [Collaborative Lesson Development Training Curriculum](https://carpentries.github.io/lesson-development-training/)

A lesson designed to teach skills and good practices in lesson design,
lesson website development, and collaboration via GitHub. Community
members can apply to join this training, and/or follow the curriculum in
their own time.

### [Choosing a Narrative and Dataset for a Lesson](/resources/curriculum/narrative-example-data.md)

Guidance for lesson developers when choosing a narrative for their lesson and example data to include in it.
Includes lists of points to consider when choosing a narrative and example dataset, and associated information about licensing and the publication of data.

### [Pilot Workshop Feedback Survey Template](https://docs.google.com/forms/d/1OGCQBotD2nOJkc7KpFZLhFfb3EBcxEDwHz_3p48qz3U/template/preview)

The standard Carpentries pre- and post-workshop surveys do not support
lesson pilots so you will need to create your own surveys to send out
before/after a pilot workshop. Although surveys for pilot workshops will
frequently include questions that are specific to the particular lesson
being piloted, there are some standard feedback questions that can be
asked after a pilot to assess the design and flow of the lesson. This
[template post-pilot workshop
survey](https://docs.google.com/forms/d/1OGCQBotD2nOJkc7KpFZLhFfb3EBcxEDwHz_3p48qz3U/template/preview)
can be copied and adapted to suit the needs of your lesson, and shared
with learners in place of the standard post-workshop survey.

### [Lesson Pilot Workshops](/resources/curriculum/lesson-pilots.md)

Information about why and how we test new lessons in workshops, including guidance and templates for hosts and instructors of pilot workshops to use.

### Beta Announcement Templates

A [template beta announcement blog
post](https://docs.google.com/document/d/1z8QmxDIiew-p1d8aLzXa0vt0FLUHNtK3oS3tucyrRsI/edit?usp=sharing)
and [template beta announcement email
message](https://docs.google.com/document/d/1hHnm-Ljb_o_rNd9bvQ83ilq40KoGoEfMPTSrFS4QOj8/edit?usp=sharing)
to publicise the beta version of a lesson. These can be used to call for
community members to volunteer to host a beta pilot workshop to aid the
ongoing development of the lesson.

### [Curriculum Onboarding Materials](/resources/curriculum/curriculum_onboarding.md)

Guidance for developing materials that will help instructors prepare to teach your new lesson or curriculum.

### [Lesson Release Process](/resources/curriculum/lesson-release.md)

A description of how to prepare a lesson release and publish it to Zenodo.

