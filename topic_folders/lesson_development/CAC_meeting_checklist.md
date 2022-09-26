## Meeting Checklist and Email Templates

### Meeting Checklist

- [Secretary] Create availability poll using [whenisgood](http://whenisgood.net/Create) (or similar service). 
  Be sure to enable the “use timezones” feature.
    - This checklist below assumes that you will gather availability from committee members each time,
      but you may find it easier to schedule several meetings at once. 
      For example, you might schedule quarterly meetings for a whole year 
      assuming that the day/time that works for the committee in one quarter 
      (e.g. 14:00 UTC on the third Tuesday of the month)
      will also be a good fit 3, 6, and 9 months later.
      If you would like to take this approach, 
      make sure to discuss it with the rest of the committee first and
      be alert to potential complications caused by seasonal clock adjustments
      (e.g. daylight savings in North America and Europe).
- [Secretary] Start scheduling meeting using this [email template](#scheduling-meeting). 
- [Secretary] Determine the best meeting time (or two if needed) from the availability poll. 
  Create an event time announcement using [TimeandDate](https://www.timeanddate.com/worldclock/fixedform.html) 
  (or similar service). Include event time announcement link in all communications about meeting times. 
- [Secretary] Set up meeting room with Zoom (or similar service). If you need a room provided by The Carpentries, 
  contact [team@carpentries.org](mailto:team@carpentries).
- [Secretary] Set up Etherpad. For first meeting, create Etherpad by visiting your desired URL starting 
  with `https://pad.carpentries.org/` (e.g. `https://pad.carpentries.org/my-cac-name`). This will create an Etherpad
  pre-populated with standard language about The Carpentries. For subsequent meetings, use the same Etherpad. 
  The history will automatically archive. Include on Etherpad:
     - Meeting connection information (Zoom link and dial in options)  
     - Time zone converter link for meeting time
     - Sign-in
     - Meeting roles (leave blank for Chair to fill in)
     - Agenda (leave blank for Chair to fill in)
- [Secretary] Send meeting invitations on Google Calendar. Include Etherpad and Zoom connection link in invite. 
- [Secretary] Send meeting announcement using this [email template](#meeting-announcement).
- [Chair] Determine meeting roles using a randomizer like [random.com](https://www.random.org/lists/).
- [Chair] Create agenda on Etherpad, collecting agenda items from:
  - Issues and pull requests tagged to the CAC on GitHub.
  - Requests that have come in by email to the TopicBox or from The Carpentries Core Team. 
  - Upcoming changes to software or changes in practice occurring in the field that should be considered by CAC. 
  - Other agenda items brought to Chair by CAC members. 
  - Each agenda item should include links to relevant conversations or information, 
    as well as an approximate length of time for discussion. Notify Secretary when agenda is ready to share. 
- [Chair] Maintain open agenda items as issues to the CAC GitHub repository. Update these with links to relevant
  conversations (e.g. tagging other issues in various lessons, or copying in emails from community members), 
  re-opening/closing issues as needed.
- [Secretary] Send meeting reminder using this [email template](#meeting-reminder).
- [Chair] Ensure that meeting proceeds smoothly using the assigned meeting roles. 
- [Secretary] Compile meeting minutes from notes. Add minutes as a PR to the GH repository using file format 
  `MONTH-minutes.md`. Include in minutes:
  - Date and time of meeting
  - Names of those in attendance
  - Agenda items discussed, a summary of each discussion, and outcomes of any votes taken
- [Chair] Review and edit or approve minutes. Merge PR. 
- [Secretary] Send meeting follow-up to group using this [email template](#meeting-followup). Include link to minutes and information about any follow-up tasks. 
- [Chair] Communicate about decisions with relevant Maintainers or other community members as needed using individual lesson repositories, mailing lists, or other channels as appropriate. 
- [Secretary] Set reminder to self to schedule next meeting. 

## Email templates

### Scheduling meeting
Subject: Scheduling [ QUARTER YEAR ] Meeting of the [ Data Carpentry / Library Carpentry / Software Carpentry ] 
[ CURRICULUM TITLE ] Curriculum Advisory Committee

Hi everyone,

I’d like to get us started on setting up our meeting for [ QUARTER YEAR ]. This meeting will be between 
[ DATE ] and [ DATE ]. 

To help schedule the meeting, could everyone please add their availability to this 
[whenisgood](link to whenisgood poll) by this coming Friday ([ DATE ])? Please make sure to put in your time zone at 
the top of the poll. I’ll look at the results and let everyone know the meeting time by [ DATE ] so that you can clear 
up any holds on your calendar.

Looking forward to our meeting. 

Best, 
[ sender name ]

### Meeting announcement

Subject: [ QUARTER YEAR ] Meeting of the [ Data Carpentry / Library Carpentry / Software Carpentry ] [ CURRICULUM TITLE ] 
Curriculum Advisory Committee

Hi all,

Thank you for providing your availability. Our [ QUARTER YEAR ] meeting will be [ TIME AND DATE IN UTC ONLY ]. 
You can check the meeting’s time in your local time zone by clicking [this link]( timeanddate link ). You should 
all have received a Google calendar invite to the meeting with Zoom connection information and the link to our Etherpad. 

A week before the meeting, I will send out our full agenda as well as meeting roles (notetaker, timekeeper, facilitator). 

Please let me know if you have any questions in the meantime or if you didn’t get the GCal invite. 

Best, 
[ sender name ]

### Meeting reminder
Subject: [ QUARTER YEAR ] Meeting of the [ Data Carpentry / Library Carpentry / Software Carpentry ] [ CURRICULUM TITLE ] 
Curriculum Advisory Committee

Hi everyone, 

Just a reminder that we’ll be meeting on [ DATE AND TIME IN UTC ONLY ]. You should have a Google Calendar invite for 
the meeting with connection information. You can double check the meeting time in your local time zone by 
[following this link]( timeanddate link ). 

[ NAME OF CHAIR ] has prepared an agenda for our meeting. Please review the agenda on [our Etherpad]( Etherpad link ) 
in advance of the meeting and be prepared to share your thoughts. 

Our roles for the meeting are also listed on the Etherpad. As a reminder, we will be using the following roles. 
If you are not able to or comfortable with carrying out your assigned role, please contact [ NAME OF CHAIR ]. 

- Facilitator - Introduces each agenda item. Monitors both the chat and the visual meeting window for “hands”, keeps 
track of order, and says whose turn it is to speak. Makes sure everyone has a chance to share their views.
- Notetaker - Records meeting attendance and major points of discussion. Especially takes note of decisions and action 
items.
- Timekeeper - Pays attention to the clock and notifies the group when time for specific agenda items is running short.

Looking forward to meeting with you all soon.

Best,
[ sender name ]

### Meeting followup
Subject: Follow-up from [ QUARTER YEAR ] Meeting of the [ Data Carpentry / Library Carpentry / Software Carpentry ] 
[ CURRICULUM TITLE ] Curriculum Advisory Committee

Hi all,

Thank you again for a very productive meeting last week. Our minutes for the meeting are posted to our repository. 
Minutes include decision points and action items for follow-up. I wanted to run these by everyone to make sure that
I’ve correctly identified the decisions that were made before [ CHAIR NAME ] follows up with the Maintainers to move
these decisions forward.

It would be greatly appreciated if you could take a look at the [minutes]( LINK TO MINUTES ) and let me know by
[ DATE AND TIME UTC ]( link to timeanddate event announcer ) if you see any problems or have any objections to the
decisions and action items. At that point, [ CHAIR NAME ] will follow up with the Maintainers on the next steps.

Thank you everyone for bringing your backgrounds and expertise to the meeting last week and for your deep thought
about this curriculum. I’m excited about [ upcoming publication or major lesson change ].

Please let me know if you have any questions or comments.

Best, 
[ sender name ]

