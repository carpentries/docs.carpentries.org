## Curriculum Advisory Committee Consultation Rubric

This rubric defines the division of responsibilities between The Carpentries Maintainers and The Carpentries Curriculum Advisory Committees (CACs).
[Roles and responsibilities](https://docs.carpentries.org/topic_folders/lesson_development/curriculum_advisory_committees.html#roles-and-responsibilities)
of Curriculum Advisory Committee members are documented elsewhere in this Handbook.
[Current committee membership can be found on The Carpentries website](https://carpentries.org/curriculum-advisors/).

### Issues over which Maintainers have full authority and which do not need CAC involvement

- Addition or removal of exercises
- Reorganization of material within episodes
- Addition or removal of callout boxes
- Addition or removal of or changes to figures
- Changes to episode timings
- Changes to lesson text

### Issues about which Maintainers should notify the CAC

- Any new versions of a dataset (either a new release or a modification of existing data)
- Any major adjustments to the lesson (e.g., episode order, passwordless access)
- Any updates to a lesson that Maintainers wish to share for informational purposes

_What to do if your curriculum does not have an active CAC?_ Maintainers do not need to notify anyone when handling issues described in the list above. ([View the list of active CACs on The Carpentries website](https://carpentries.org/curriculum-advisors/).)

### Issues that may benefit from Maintainers consulting with the CAC, but over which Maintainers retain authority

- Addition of a new library or package
- Introduction of a new topic / learning objective (e.g., [adding file permissions to LC shell lesson](https://github.com/LibraryCarpentry/lc-shell/issues/63))
- Updates to software/packages that are minor versions (e.g., Python 3.7 -> 3.8) when the new version is backwards compatible with current version
- Additions of experimental features (e.g., `git checkout` → `git restore` / `git switch`)
- Any change to a lesson that impacts the content/scope of another lesson in the curriculum
- For Incubator lessons - Review of a lesson outline where lesson developers would like the lesson to be considered for eventual adoption into
a Lesson Program’s official curriculum
- Issues which are not covered anywhere else in this rubric

_What to do if your curriculum does not have an active CAC?_ Maintainers may consult the Curriculum Team ([by email](mailto:curriculum@carpentries.org) or tagging the `core-team-curriculum` team on the relevant GitHub issue/pull request/discussion) and/or the wider community when handling issues described in the list above. For example, where more perspectives are needed, it may be helpful to use [relevant communication channels](https://carpentries.org/connect/) to call for input and feedback from the Instructor community. ([View the list of active CACs on The Carpentries website](https://carpentries.org/curriculum-advisors/).)

### Issues for which Maintainers must seek CAC approval

- Replacing the dataset used in the lesson with a different dataset. This does not include cases in which the data being used in the lesson is being updated to a
new version (e.g., a new data release) or is modified to make it more suitable for the teaching environment
(e.g., introduction of messiness to the dataset).
- Changing the software being used in the lesson. This does not include updating to a new stable, backwards-compatible version of the
existing software (e.g., Python  3.6 → 3.7.x), but does include:
  - Updating to a non-backwards compatible version of existing software (e.g., Python 2.x → 3.x, R 3.x → 4.x)
  - Change in plotting library (e.g., Matplotlib, Plotly, Seaborn, ggplot, Altair)
  - Change in libraries / packages taught (i.e., removal or replacement)
  - Change in SQL dialect (e.g., SQLite, MySQL, PostgreSQL, MSSQL Server)
  - Change in IDE being used to teach the lessons (RStudio, Jupyter Notebook)
  - Change from GitHub as remote hosting platform to a different remote hosting platform, e.g., GitLab
- Removal of an entire episode’s worth of content
- Change in lesson infrastructure (e.g., moving Genomics lessons from AWS to CyVerse)
- Retirement of a lesson (e.g., MATLAB, Mercurial)
- Addition of a new lesson to the core curriculum (e.g., adding Julia as an alternative to R / Python)
- Adding or removing prerequisites from a lesson (for curricula with multiple lessons)
- Promotion or graduation of a lesson from alpha to beta to stable. Decisions on approval can be based on recommendations from the Curriculum Team,
CAC member involvement in lesson pilot workshops, and/or open peer review of lessons in The Carpentries Lab.

_What to do if your curriculum does not have an active CAC?_ Maintainers should consult the Curriculum Team ([by email](mailto:curriculum@carpentries.org) or tagging the `core-team-curriculum` team on the relevant GitHub issue/pull request/discussion) when handling issues described in the list above. The Curriculum Team will coordinate and facilitate a discussion among community members likely to be affected by the changes (other Maintainers, Instructors, etc). ([View the list of active CACs on The Carpentries website](https://carpentries.org/curriculum-advisors/).)
