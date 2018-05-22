### Trainers Guide

#### Trainer Meetings
The Trainers group meets regularly. We have two types of meetings - business meetings, focused on discussing curricular and policy changes, and discussion meetings, where we share experiences and get advice about running instructor training events. Upcoming meetings are listed on [our Etherpad][trainer-pad] and on the [Community Calendar][community-calendar]. If you are not a Trainer, but are interested in joining a meeting, please contact Erin Becker (ebecker@carpentries.org). Minutes for these meetings [are available][trainer-minutes].

#### Signing up to Teach an Instructor Training Event

1. The Program Manager will send an email to the Trainers list asking all Trainers to fill in their calendar for the [upcoming time period](scheduling_training_events.html). Trainers should sign up for as many days as they are available and hold those dates in their calendar until the schedule is confirmed.
1. The Program Manager will confirm events with individual Trainers, at which point they are free to release all other dates on their calendar.
1. Member sites will sign up for available dates. The Program Manager will let Trainers know which sites they will be teaching as they sign up.
1. If no member site signs up one month before the event, the event will become an open instructor training or be cancelled, depending on need. The Program Manager will notify instructors of this decision.

A calendar for upcoming instructor training events is [here](http://carpentries.github.io/instructor-training/training_calendar/).

#### Trainer Checklists

##### Running an Instructor Training Event (General)

###### Four weeks before the event
-  Contact your co-Trainer(s) and decide who will teach what.  
-  Create an event Etherpad (using the [Etherpad template][etherpad-template]) or Google Doc and a workshop website (using the [training template][training-template]).  
-  Send Etherpad/Google Doc and website links to training@carpentries.org.  

###### Two weeks before the event
-  Introduce yourself to your trainees.  

###### One week before the event (if teaching remotely)   
-  Test videoconferencing set up with co-Trainer(s) using login credentials provided.   
-  Plan logistics with co-Trainer(s).  
-  Decide with co-Trainer(s) whether all Trainers should be present for the full event or if you will log on during your scheduled teaching times only.  
-  Make a copy of the [Virtual Minute Cards template][minute-cards-template] and personalize for your event.  

###### During the event
-  Take attendance.  
-  Remind trainees to fill out application (member events only).   
-  Remind trainees to sign up for demo, discussion (links in [checkout checklist][checkout-checklist]).  
-  Monitor the Etherpad / Google Doc for questions and responses to exercises.  
-  If teaching remotely: Turn off video during long exercises and coffee breaks and disconnect during lunch.  

###### Immediately after the event
-  Send a list of those who completed the training to checkout@carpentries.   
-  Send an email to trainees thanking them for participating and linking to [checkout checklist][checkout-checklist] using [this template](email_templates.html#email-after-training-event)  
-  Review survey results and prepare to discuss at upcoming [Trainers discussion meeting][trainer-pad].  
-  File any relevant issues or PRs to the [instructor training repo][training-repo].  

###### Long-term after the event 
-  Join a [Trainer discussion meeting][trainer-pad] to discuss how your event went.   

#### Differences Between In-person and Online Training Events

##### In-person trainings
- When watching videos, project them to the whole group.   
- Assign (or let participants select) physical breakout groups.  
- Use physical sticky notes to get minute card feedback at lunch breaks and end of each day.  

##### Online trainings (a few small groups) 
- When watching videos, have one Trainer do a screenshare with their audio on or have one person in each group play the video for the participants at their site.  
- Assign (or let participants select) physical breakout groups.  
- Use the [virtual minute card][minute-cards-template] form to get feedback at lunch breaks and end of each day.  
- Have participants do all small-group exercises with participants at same site.  

##### Online trainings (completely distributed)  
- When watching videos, have all participants watch separately.  
- Assign breakout groups randomly to breakout rooms in Zoom. Be sure to remove Trainers and helpers when assigning groups. 
- Use the [virtual minute card][minute-cards-template] form to get feedback at lunch breaks and end of each day.  
- Have participants screen share with their breakout room during the live coding exercises.   
- For exercise to set up a workshop website, put participants in breakout rooms and have one person screen share while the others help guide them verbally.  

#### Zoom Manual (Online Trainings)
Online Carpentry Instructor Training events are held on [Zoom][zoom-home]. You can set up a personal Zoom account for yourself for free. This personal account will be able to attend the training event (or any other online Carpentry event), but will not be able to act as host.   

About a week before your event, you will be given login credentials for a Carpentry account. This account will be the host for the event and will have extra privileges including the ability to mute participants and assign participants into breakout rooms. Decide ahead of time with your co-Trainer(s) who will log-in with these credentials. The host can transfer host privileges to other participants, so you will be able to trade host status back and forth with your co-Trainers during the event.  

All Carpentry online events are set up such that participants can enter the room without the host being present. If you ever get an error message saying you can’t join the room because you’re not the host, please contact Carpentry staff immediately.

##### Host abilities:  
- “Mute” is in the lower left. To mute other participants, the host can go to “Manage Participants”, hover over a participant’s name, and click “mute”.  
- When the room host clicks “End Meeting” a dialogue box appears with three options: “Cancel”, “Leave Meeting” and “End Meeting for All”. Be careful not to end the meeting if you are leaving the room while your co-Trainer teaches.  
- Only the host has the ability to create “Breakout rooms”. The button for this is on the lower left. Breakout rooms can be assigned automatically. By default, participants will be assigned to the same groups each time breakout rooms are used. You can change participants assignments manually if desired.  
- The host can move between breakout rooms and can send messages to all rooms simultaneously.  

##### General tips:  
- “Gallery view” in the upper right toggles the display to show more participants videos.  
- “Share screen” is at the bottom middle of the screen. To end “share screen” you click the red button that will appear at the top middle of the screen when you are in screen sharing mode.  
- When you screen share, you have the option to share individual apps or your entire desktop. The default is the full desktop.  
- The Zoom chat is not stable (it is not saved across sessions or after going into breakout rooms). We highly recommend using the Etherpad or Google Doc chat instead.  

#### Running a Teaching Demonstration  

If you would like to watch an example teaching demo, there is a recording of one [here][demo-video].

##### Before the demo
-  Sign up to [lead demos][demo-pad].  
-  For each trainee, pick a suitable starting point in the lesson that they have chosen. For most lessons, any episode will be suitable. There are a few exceptions - [listed below](#not-good-starting-points-for-demos). Do not have them start in the middle of an episode. Note that some lessons (e.g., the Software Carpentry R lesson using inflammation data) have supplementary episodes. Do not pick from those.  

##### Shortly Before the Demo
-  Go to the Zoom room. The link is in the [Etherpad][demo-pad].    
-  Once everyone is in the call (audio and video working), remind them of the Code of Conduct, explain the procedure for the demo session, and remind them that trainees have to be able to teach from any episode from their chosen lesson. Ask whether anyone has only prepared for 5 minutes from one episode instead of the entire lesson, and if so, suggest strongly they reschedule.    
-  Ask those not presenting to mute their microphone, and tell them they are to give feedback in the Etherpad using the same positive-vs-negative and content-vs-presentation rubric used in training.    
-  Hand out the assignment to the first trainee, give them a bit of time to set up the demo (they may have to import some packages, load some data, move to a certain folder etc).  
-  Ask them to share their screen using the “Share Screen” lower menu in Zoom.  
-  Once they are ready, give them a 3-2-1 countdown to start.  
-  Use a countdown timer which makes a noise once their 5 minutes are up (e.g., your phone), or just say “bong” really loudly at the end of their time.  
-  After the five minute timer, allow them to finish their sentence and tell them time’s up.
-  Use a [rubric][demo-rubric] for notes.   
-  After the trainee is finished, first ask how they themselves thought it went, then give constructive feedback based on your notes.  
-  Do NOT tell a trainee whether they passed immediately after their demo.   
-  Repeat for the other trainees.  
-  At the end of the season, ask for general questions.  
-  If all of your trainees passed, you can tell the group at the end of the demo session. If anyone did not pass, tell everyone you will send them each an email to let them know if they passed.  

##### After the Demo 
-  Email checkout@carpentries.org with names, pass/fail, and SWC/DC for each of your trainees.  
-  Clear Etherpad of data from your session.  
-  Send each trainee an email letting them know they [passed](email_templates.html#trainee-did-pass-teaching-demo) or [did not pass](email_templates.html#trainee-didnt-pass-teaching-demo) the teaching demo. If needed, let them know the reason they did not pass and asking them to retry.

##### Not Good Starting Points for Demos
Any episode other than those listed below should make an okay starting point for a teaching demonstration. 

*  SWC
  * [The Unix Shell](http://swcarpentry.github.io/shell-novice/)
    * [Introducing the Shell](https://swcarpentry.github.io/shell-novice/01-intro) - no live coding
  * [Version Control with Git](http://swcarpentry.github.io/git-novice/)
    * [Automated Version Control](https://swcarpentry.github.io/git-novice/01-basics/) - no live coding
    *  anything after [Tracking Changes](https://swcarpentry.github.io/git-novice/04-changes) - dependencies
  * [Version Control with Mercurial](http://swcarpentry.github.io/hg-novice/)
    *  [Automated Version Control](https://swcarpentry.github.io/hg-novice/01-basics/) - no live coding
    *  anything after [Tracking Changes to Files](http://swcarpentry.github.io/hg-novice/04-tracking/) - dependencies
  * [Using Databases and SQL](http://swcarpentry.github.io/sql-novice-survey/)
    *  [Data Hygiene](https://swcarpentry.github.io/sql-novice-survey/08-hygiene/) - no live coding
  * [Programming with Python](http://swcarpentry.github.io/python-novice-inflammation/)
     * [Debugging](https://swcarpentry.github.io/python-novice-inflammation/09-debugging/) - no live coding
  * [R for Reproducible Scientific Analysis](http://swcarpentry.github.io/r-novice-gapminder/)
     * [Writing Good Software](https://swcarpentry.github.io/r-novice-gapminder/16-wrap-up/) - no live coding
  *  [Automation and Make](http://swcarpentry.github.io/make-novice/) 
      * anything after [Makefiles](https://swcarpentry.github.io/make-novice/02-makefiles/) - dependencies

*  DC (published lessons only)
  * Ecology
     * [Data Cleaning with OpenRefine](http://www.datacarpentry.org/OpenRefine-ecology-lesson/)
        * anything after [Working with OpenRefine](http://www.datacarpentry.org/OpenRefine-ecology-lesson/01-working-with-openrefine/) - dependencies
    * [Data Management with SQL](http://www.datacarpentry.org/sql-ecology-lesson/)
      * [Databases using SQL](http://www.datacarpentry.org/sql-ecology-lesson/00-sql-introduction/) - live coding doesn't start until middle of episode
    * [Data Analysis and Visualization in R](http://www.datacarpentry.org/R-ecology-lesson/)
        * [Before We Start](http://www.datacarpentry.org/R-ecology-lesson/00-before-we-start.html) - no live coding  
        * anything after [Manipulating data frames](http://www.datacarpentry.org/R-ecology-lesson/03-dplyr.html) - dependencies
    * [Data Analysis and Visualization in Python](http://www.datacarpentry.org/python-ecology-lesson/)
        * anything after [Data workflows and automation](http://www.datacarpentry.org/python-ecology-lesson/05-loops-and-functions/) - dependencies
   * Genomics 
      * TBA
   * Social Sciences
     * [Data Cleaning with OpenRefine for Social Scientists](http://www.datacarpentry.org/openrefine-socialsci/)
        * anything after [Working with OpenRefine](http://www.datacarpentry.org/openrefine-socialsci/02-working-with-openrefine/) - dependencies
      * [Data Analysis and Visualization with R for Social Scientists](http://www.datacarpentry.org/r-socialsci/)
        * [Before We Start](http://www.datacarpentry.org/r-socialsci/00-intro/) - no live coding  
        * anything after [Introducing dplyr and tidyr](http://www.datacarpentry.org/r-socialsci/03-dplyr-tidyr/) - dependencies

[trainer-agreement]: ../instructor_training/trainers_guide.html#trainer-agreement
[trainer-process]: ../instructor_training/trainers_training.html
[trainer-pad]: http://pad.software-carpentry.org/trainers
[community-calendar]: https://software-carpentry.org/join/#community-events
[trainer-minutes]: https://github.com/carpentries/trainers/tree/master/minutes
[etherpad-template]: http://pad.software-carpentry.org/ttt-template
[training-template]: https://github.com/swcarpentry/training-template
[minute-cards-template]: https://docs.google.com/forms/d/1ZvNx2co9BLEBTzDavUE7ZkAhkekBa19_5aIRFAdQIqw/edit
[checkout-checklist]: http://www.datacarpentry.org/checkout/
[training-repo]: http://carpentries.github.io/instructor-training/
[zoom-home]: https://www.zoom.us/
[demo-video]: https://www.youtube.com/watch?v=FFO2cq-3PPg
[demo-pad]: http://pad.software-carpentry.org/teaching-demos
[demo-rubric]: https://github.com/carpentries/instructor-training/blob/gh-pages/files/teaching-demo-rubric.md


