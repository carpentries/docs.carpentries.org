
## Steps for Maintainer Onboarding process

1) Application to become a Maintainer is [here](https://docs.google.com/forms/d/1PMzhri0CmbNkJiNor-nXDOP0d5jlAyp-VF-3df6cUf0/edit). Will need to create a new version or delete existing responses. Also need to change intro text.

2) Process so far has been to accept all applications from people who are at least somehow involved in the community. So far (1/26/18) there has only been one application that was not accepted.

3) After reviewing applications for any red flags, send accepted applicants invitation to become a Maintainer template email.

To set up a scheduling poll, use [WhenIsGood](http://whenisgood.net/). Click "Use Timezones" and then "SHOW OPTIONS".
Unselect Sunday and Saturday. Add Duration = 60 minutes. Select "hide dates".

4) Add Maintainers who are going through training to [maintainer-onboarding Google Group](https://groups.google.com/a/carpentries.org/forum/#!forum/maintainer-onboarding). This is where announcements about upcoming meetings will be sent out.

5) After deadline has passed for responding to scheduling poll, select the two times that maximize attendance. This needs to be done manually from the whenisgood results, as there isn't a "choose two times" option.

6) Set up [Maintainer onboarding Etherpad](http://pad.software-carpentry.org/maintainer-onboarding) with meeting dates and times. Use [timeanddate meeting time announcer](https://www.timeanddate.com/worldclock/fixedform.html) links to make it easy for people to convert meeting times to their own time zone.

7) Send out an email to the Google Group letting everyone know about the scheduling. See template email (Maintainer Onboarding Meetings). 

8) One week before the first onboarding meeting, send a reminder email to the Google Group. See template email (Reminder - Onboarding starts next week). 

9) Run the three weeks of meetings according to [the curriculum](https://carpentries.github.io/maintainer-onboarding/). Keep record of who participates.

10) If people are not able to make all of the meetings, ask them to write out responses to the discussion questions and homeworks. See template email (Unable to attend Maintainer onboarding).

11) After the final onboarding meeting, do the following for each of the Maintainers who have completed the onboarding requirements:  
- Give them "write" access to their lesson repository on GitHub. 
- Add their name to the lesson table on the website.
- Award them a Maintainer badge in AMY.

12) Send email to the Maintainers email list announcing new Maintainers. See email template (Welcome New Maintainers).

13) Send an email to those who did not complete the requirements. See email template (Opportunities to complete Carpentry Maintainer onboarding).

14) Repeat step 11 as needed for those who complete requirements by email. 

## Template emails

Subject: Invitation to become a Carpentry Maintainer
CC: Existing Maintainers for the repo and other new Maintainer applicants for the same repo.

Hi all,

Thank you for applying to become a Maintainer for {lesson name and link to repo}. We're excited to have you on the Maintainer team! Your co-Maintainers are cc'd here.

As a Maintainer, you’re part of a team that is responsible for ensuring that your lesson materials stay up-to-date, accurate, functional and cohesive. You’ll monitor your lesson repository, make sure that PRs and Issues are addressed in a timely manner, and participate in the lesson development cycle including lesson releases. {Add a sentence about when the next lesson release is scheduled for.}

The new Maintainers for all of the Carpentry lessons will be meeting a few times before {month} for onboarding and training in the Carpentry maintenance workflow. Please fill out this schedule poll {add link to poll} by {deadline} with your general weekly availability. Our first meeting is tentatively set for the first week in {month} and we will be meeting three times. Don't forget to select your timezone before filling out your availability. We have new Maintainers joining the team from all over the world, so please be as flexible as possible. 

New Maintainers will be given write access to their lesson repos after completing the onboarding process. In the meantime, please start becoming familiar with your lesson materials, sign up for the [Maintainer mailing list](http://carpentries.topicbox.com/groups/maintainers), and check out the dates of the next [Maintainer general meeting](http://pad.software-carpentry.org/maintainers). You're more than welcome to start attending Maintainer meetings before our onboarding. Please let me know if you have any questions. Looking forward to seeing you in March!

Best,
{name}

--------------------

Subject: Maintainer Onboarding Meetings

Hi everyone,

Thank you for adding your availability to the scheduling poll. Based on everyone's responses, we will be meeting at two different times. You do not need to attend the same meeting each week, and I would actually encourage those who can do so to switch which meeting they attend so that we can all meet one another over the course of the onboarding.

We will be meeting for three weeks, starting the week of {date}. You can see the meeting times in your local time zone on [our Etherpad](http://pad.software-carpentry.org/maintainer-onboarding). If you know that you will need to miss one of our meetings, please let me know as soon as possible so that we can make alternative arrangements for you to complete the training.

Before our first meeting, please:

1) Sign up for the [Maintainer mailing list](http://carpentries.topicbox.com/groups/maintainers). This is a low-volume channel for communicating about issues relevant to the Maintainer community.

2) Add Maintainer meetings to your schedule. The meeting times are listed on the [Maintainer Etherpad](http://pad.software-carpentry.org/maintainers) and on the [Community Calendar](https://software-carpentry.org/join/#calendar). The Maintainer monthly meetings are not mandatory, but are encouraged as a way of getting to know the more experienced Maintainers.

If you have any questions, please let me know.

Looking forward to meeting all of you next month!

Best,
{name}

--------------------

Subject: Reminder - Onboarding starts next week

Hi all,

Just a quick reminder that we'll be starting our onboarding meetings next week. Please sign up for one of the two available sessions on our groups [Etherpad](http://pad.software-carpentry.org/maintainer-onboarding). 

During our meetings, we'll be test-running a [new curriculum for Maintainer Onboarding](https://carpentries.github.io/maintainer-onboarding/index.html). Your suggestions and pull requests to this repository are more than welcome! This curriculum will form the basis for onboarding of new groups of Maintainers in the future, so please help to improve it. 

Before our first meeting, please look at the first lesson in the Maintainer Onboarding curriculum ([Social Aspects of Lesson Maintenance](https://carpentries.github.io/maintainer-onboarding/01-social/index.html)) and do your best to work through the exercises marked "Preparatory Homework".

Looking forward to seeing you all soon. Let me know if you have any questions.

Best,
{name}

--------------------

Subject: Unable to attend Maintainer Onboarding

Thanks for letting me know. What I'm doing for people who have to miss a session is asking that they send me an email with their responses to the homeworks (including the preparatory homeworks) and discussions. Could you please take a look through the first lesson and send me your thoughts sometime next week?

Best,
{name}

--------------------

Subject: Welcome New Maintainers!

Today I'm happy to announce the addition of {number} new Maintainers to our team. Please join me in welcoming: 

{Table of names and lessons for new Maintainers}

Each of these new Maintainers has gone through a three week onboarding program to help prepare them for the complex role that Maintainers serve in our community. We certainly couldn't cover everything in these three meeting! Please help your new team mates as they run into snags  and feel free to reach out to me with any questions or concerns. 

Looking forward to seeing everyone in action!

Best,
{name}

--------------------

Subject: Opportunities to complete Carpentry Maintainer onboarding

Hi all,

Thank you again for volunteering to act as a Carpentry Maintainer. You're getting this email because you expressed interested in being a Maintainer but were not able to attend the onboarding sessions. If you are still interested in becoming a Maintainer, please choose one of the two following paths:

1) Reading through the three Maintainer Onboarding episodes, writing up your responses to the discussion questions and homeworks, and sending me your responses by {deadline}.

or

2) Joining the next Maintainer Onboarding session, which will be held in {month}. 

Please let me know as soon as possible which of these two paths you'd like to follow, or if you are no longer interested in joining the Maintainer team.

Looking forward to hearing back from you.

Best,
{name}
