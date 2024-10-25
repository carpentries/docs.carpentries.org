# Lesson Development Roles
Creation of a new lesson or curriculum is a collaborative process, usually involving many community members taking up different roles. It is also [an iterative process](./lesson-life-cycle.md), meaning that a lesson can always be considered as under development to some extent.

This page describes the different roles people can take in the design, development, testing, and maintenance of a new lesson or curriculum.

* [Lesson Developers](#lesson-developers)
* [Pilot Workshop Instructors](#pilot-workshop-instructors)
    * [Alpha Pilot Instructors](#alpha-pilot-instructors)
    * [Beta Pilot Instructors](#beta-pilot-instructors)
* [Maintainers](#maintainers)
* [Reviewers](#reviewers)

## Lesson Developers
A lesson may have one or several initial developers. Developers draft the lesson content, figures, and code and create appropriate challenge problems. The team of developers should have among them both appropriate domain experience -- working in the same field as the intended audience for the materials -- and programmatic experience –- regularly using the tools for which they are developing lessons in their own work. From a technical standpoint, lesson developers will also need to be familiar with the infrastructure that we use for developing and hosting The Carpentries lessons: primarily git, GitHub, and Markdown and/or R Markdown. If you’re not comfortable with any or all of these tools, some of the resources listed below can be used to learn and practice with them.

Drafting a lesson is only one part of the development process: new lessons need to be thoroughly tested in [_pilot workshops_](./lesson_pilots.md), adjusted in response to feedback, then updated and maintained in the longer term. [This life cycle of a lesson is discussed in more detail elsewhere in this handbook](./lesson_life_cycle.md).

### Resources for Lesson Developers
- Our [Collaborative Lesson Development Training](https://carpentries.github.io/lesson-development-training/) teaches principles and good practices in curriculum design and development, and collaboration skills to help the lesson development team work together effectively. It also introduces the fundamentals of creating accessible lesson content with The Carpentries Workbench -- the tools we use to build lesson websites from source files in a GitHub repository.
- [Introduction to The Carpentries Workbench](https://carpentries.github.io/sandpaper-docs/) provides more comprehensive documentation of the lesson infrastructure.
- [A Primer on Markdown and GitHub](https://carpentries.github.io/lesson-development-training/instructor/markdown-github-primer.html) links out to two resources teaching the fundamentals of two tools central to lesson development in The Carpentries.


## Pilot Workshop Instructors
Our lessons are primarily intended to be taught in workshops, and their design and content should be tested out in that setting. Feedback should be collected during the workshop and incorporated into the lesson. We refer to the events where a new lesson is tested as _pilot workshops_.
[The Lesson Pilot Workshops section of this handbook](./lesson_pilots.html) provides more information about these events, including templates and guidance on event logistics.

### Alpha Pilot Instructors
It is common – but not essential – that the instructors for the first pilot of a new lesson will be the original lesson developers. We refer to these events as _alpha pilots_ and they present a great opportunity to gather information and get early feedback to inform the further development of the content. In addition to collecting feedback from learners, alpha pilot instructors should take extensive notes during the event. We recommend that pilot instructors meet as soon as possible after the workshop, or at the end of each teaching session, to debrief their experience and prepare a list of action points for lesson developers to address to improve the lesson. 

### Beta Pilot Instructors
If the new lesson is being considered for adoption into The Carpentries official curriculum, instructors for these beta pilot workshops should be certified Carpentries Instructors who have previously taught at least two Carpentries workshops. Instructors with this level of experience will be more prepared to troubleshoot issues that arise during the workshop, and more likely to provide useful feedback after the workshop. Beta pilot instructors may be Maintainers, Curriculum Advisors, or any Carpentries community member other than the original lesson developers. In fact, recruiting beta pilot instructors who are already playing active roles in the lesson is likely to be fruitful, as these people are invested in bringing the lesson to maturity. For two beta pilot workshops, you will need at least four instructors. Lesson authors should plan to meet virtually with pilot instructors before the workshop to answer questions and provide any technical help with setup.

### Resources for Pilot Workshop Instructors
- [The Lesson Pilot Workshops section of this handbook](./lesson_pilots.md) includes more information about the purpose of lesson pilots, guidance for lesson developers and hosts, templates for communications and feedback surveys, etc.
- The [Preparing to Teach](https://carpentries.github.io/lesson-development-training/preparing.html) episode of Collaborative Lesson Development Training provides guidance for lesson developers planning alpha pilots for a new lesson.

## Maintainers
Lesson Maintainers are essential for the long-term viability of a lesson. As a lesson is taught, new instructors and learners identify potential places for improvement - whether correcting a typo, simplifying code, or suggesting a significant shift in the narrative of a lesson. Maintainers proactively monitor their lesson’s GitHub repository to make sure that issues and suggestions for improvement are addressed in a timely manner. Maintainers also play a vital role in communicating with contributors, ensuring that our community lives up to its ideals in welcoming and appreciating contributions from everyone - from first-time contributors to long-time members of The Carpentries community.
People acting as Maintainers should be experienced with the tools that are taught in the lesson, ideally using it daily or weekly in their own work. In addition, they should have experience working in a relevant domain related to the lesson, and/or experience working with GitHub and the other technologies we use to create and host our lessons. Each lesson should have at least two Maintainers, and it is beneficial for those Maintainers to have a diversity of experience levels with the domain and technical aspects of the lesson – and the tools for maintenance.

### Resources for Maintainers
- The [Maintainers Handbook](../../handbooks/maintainers.md) includes guidance on communications, lesson repository management, and other aspects of the role.
- The [Maintainer Onboarding curriculum](https://carpentries.github.io/maintainer-onboarding/) contains the information we provide to Maintainers for official Carpentries lessons when they begin the role.
- [Introduction to The Carpentries Workbench](https://carpentries.github.io/sandpaper-docs/) provides more comprehensive documentation of the lesson infrastructure: the tools we use to build lesson websites from source files in a GitHub repository.


## Curriculum Advisors
While lesson developers and Maintainers handle the day-to-day improvement and upkeep of lessons, Curriculum Advisors provide higher level guidance on the direction of that development. Curriculum Advisors should be experts in the domain of the lesson, and aware of the way the skills it teaches are (or need to be) applied in that domain. Curriculum Advisors take responsibility for guiding the development of a whole [curriculum](./curriculum-structure.md): where that curriculum consists of multiple lessons, Curriculum Advisors should consider how it needs to develop as a whole – and how changes in one lesson might impact the others.

If a new lesson is intended to be incorporated into an existing curriculum, the lesson developers should consult the existing Curriculum Advisory Committee about their plans as early in the development process as possible. For example, lesson developers might share an overview of the planned design and content of the lesson before investing a lot of time in creating material. This early consultation allows Curriculum Advisors to comment on the planned lesson, evaluate how easily it will fit into the existing curriculum, and consider the impact it may have on other lessons therein.

### Resources for Curriculum Advisors
The [Curriculum Advisors Handbook](../../handbooks/curriculum-advisors.md) includes more information on the role, the logistics of how Curriculum Advisory Committees are run, etc.


## Reviewers
Feedback is essential to the development of an effective lesson. The primary goal of [pilot workshops](./lesson-pilots.md) is to provide feedback that developers can use to improve the design and content of their new lesson. In this regard, instructors at pilot workshops can be considered important reviewers, especially those who conduct and provide feedback from beta pilots. Nevertheless, it can be beneficial to invite additional feedback from reviewers. Reviewers should focus their assessment of a lesson on its utility as an accessible learning and teaching resource, its suitability for its stated target audience, and the accuracy of its content.
Lesson developers can find reviewers through their own networks, or by communicating with the wider community to call for volunteers. Reviewers might provide feedback and suggest improvements directly, in the form of issues and pull requests on the lesson repository, or via email/discussion. The Carpentries also hosts a platform for structured, open peer review of lessons by the community.

### Open Peer Review of Lessons in The Carpentries Lab
[The Carpentries Lab](https://carpentries-lab.org/) hosts community-owned lessons that have passed peer review, and provides a platform for the process of peer review to take place.
Reviews exist as publicly-visible issue discussions on [the Lab Reviews repository](https://github.com/carpentries-lab/reviews/). Members of The Carpentries community volunteer as Reviewers and Editors for the Lab.

### Resources for Reviewers
* Documentation on the Carpentries Lab Reviews repository provides [more information about the peer review process](https://github.com/carpentries-lab/reviews?tab=readme-ov-file#what-is-the-process-for-submitting-a-lesson-to-the-carpentries-lab), and [the guidance provided to Reviewers](https://github.com/carpentries-lab/reviews/blob/main/docs/reviewer_guide.md).
* The Carpentries [Collaborative Lesson Development Training](https://carpentries.github.io/lesson-development-training/) provides guidance on best practices in lesson design and content development, which can be used to inform lesson reviews.

