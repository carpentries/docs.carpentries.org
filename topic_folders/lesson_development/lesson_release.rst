Release Process and Schedule
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Lessons are released on a 6-month release cycle. Lesson releases are
named by the year and month they happen, e.g., ``2016.05``.

1. Each lesson lives in the ``gh-pages`` branch of its own repository.
2. When a release is made, the lesson Maintainer(s) create a branch
   named after the release, e.g., ``2016.05``.
3. A Release Maintainer generates HTML pages for that release and adds
   them to the branch.
4. If there isn’t already a directory for that release in the
   ```swc-releases``
   repository <https://github.com/swcarpentry/swc-releases/>`__, the
   Release Maintainer creates one and adds an ``index.html`` page to it.
5. The Release Maintainer adds a submodule to the release directory of
   ```swc-releases`` <https://github.com/swcarpentry/swc-releases/>`__
   that points to the newly-created release branch of the lesson.

More information about lesson releases coming soon!

Lesson Release Checklist
~~~~~~~~~~~~~~~~~~~~~~~~

**For each lesson release, copy this checklist to an issue and check off
during preparation for release**

| Scheduled Freeze Date: YYYY-MM-DD
| Scheduled Release Date: YYYY-MM-DD

Checklist of tasks to complete before release:

-  ☐ check that the learning objectives reflect the content of the
   lessons
-  ☐ check that learning objectives are phrased as statements using
   action words
-  ☐ check for typos
-  ☐ check that the live coding examples work as expected
-  ☐ if example code generates warnings, explain in narrative and
   instructor notes
-  ☐ check that challenges and their solutions work as expected
-  ☐ check that the challenges test skills that have been seen
-  ☐ check that the setup instructions are up to date (e.g., update
   version numbers)
-  ☐ check that data is available and mentions of the data in the
   lessons are accurate
-  ☐ check that the instructor guide is up to date with the content of
   the lessons
-  ☐ check that all the links within the lessons work (this should be
   automated)
-  ☐ check that the cheat sheets included in lessons are up to date
   (e.g., RStudio updates them regularly)
-  ☐ check that language is clear and free of idioms and colloquialisms
-  ☐ make sure formatting of the code in the lesson looks good
   (e.g. line breaks)
-  ☐ check for clarity and flow of narrative
-  ☐ update README as needed
-  ☐ fill out “overview” for each module - minutes needed for teaching
   and exercises, questions and learning objectives
-  ☐ check that contributor guidelines are clear and consistent
-  ☐ clean up files (e.g. delete deprecated files, insure filenames are
   consistent)
-  ☐ update the release notes (NEWS)
-  ☐ tag release on GitHub

Upcoming Lesson Releases
~~~~~~~~~~~~~~~~~~~~~~~~

Information about upcoming lesson releases - coming soon!
