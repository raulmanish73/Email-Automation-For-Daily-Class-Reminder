# Email-Automation-For-Daily-Class-Reminder
Build a automation to send daily class reminder 24 hour before the class if class is on Tue, Wed, Thu, Fri and send the reminder on Fri if class happen on Monday. 


You need to create a email reminder program for the students of a course series which sends reminder email to the students just before the class day. But if the class happens on Monday, the reminder should go on Friday. (the class will happen only on weekdays)

Currently only one student has enrolled in the course with the
mail id: manishraul20@gmail.com
name: MAnish R

The schedule of the class is given in schedule.txt in the below format (mentioning the dates on which the class will happen along with topic name separated by '-'.) (the file is provided at this link, please download the file - https://drive.google.com/file/d/1m0Vuy-_2RIlMAdC9xPBqKAZ6Yev-xP7-/view?usp=sharing

Important Notes:

Please create a reminder_mail.py file which executes the above email reminder program.

The email reminder program reminder_mail.py should be run everyday at 12:00 PM by automatic scheduling so that the student gets the mail one day before the class on 12:00 PM. For eg. if the class is on Friday, the student should get the mail on Thursday 12:00 PM.

The emails should be sent from your email id to the students email id.

The email's subject and body should be written in the below manner
Subject - OneLearn course series reminder

body - This is a reminder mail for your class on <Topic name of the day taken from schedule.txt> at <given date and time from schedule.txt>. Please join the class on time.

For eg. for the class on 8 nov 2021, the mail will go out on 12:00PM on 5 Nov (as 8 nov is monday). The mail's subject and body will be
Subject - OneLearn course series reminder

Body - This is a reminder mail for your class on Class 1 Mod 1 at 2021 8 Nov 10:00 AM. Please join the class on time.

Once you are finished with the script, you need to put the script for automatic scheduling for 8 days. The script will be sending mails to the student according to the above schedule.txt file requirement.(we will monitor if we are getting the appropriate mails or not). Remember that when there is no class the next day, don't send any email. (Specifically if the class is on Monday, don't send any reminder mail on Sunday for it, it should be sent on prior Friday)
Additional Notes:

Automatic scheduling of email can be done using the 'Task Scheduler' Program in windows. After 8 days you may need to delete the daily automatic schedule of email reminder program.

Automatic scheduling will be running from your computer so remember that you may need to open your computer around 12:00 PM everyday when your program is running. You need to have the reminder_mail.py on your computer in order to run this script everyday from your computer.

You can use this tutorial to learn how to send emails and run automatic scheduling program - https://onelearn.notion.site/Email-Reminder-Program-Tutorials-8b9e612a7a7046588c4c2e26661a7a94

You need to work with smptlib library in order to send emails and login to your email id using the script file. When you are logging in you will need to provide your email id and password to the program. Please provide these two parameters as command line arguments to the script, don't put them in the script file reminder_mail.py as it might lead to privacy voilation of your details.

Please share reminder_mail.py file with us after you complete the program.

Evaluation Criteria

Completion and correctness of the code
Efficient use of functions in order to solve the complete problem (testing your coding plus breakup of problem statement).
Logic used to build the reminder functionality
User friendly variable names and function names. We will also check if you have done proper modules imports or not.
Ensuring that none of the personal information comes up in reminder_mail.py file that you share with us.
PS: Please inform us before you start automatic scheduling. We will monitor the mails for the next 8 days to check if your script is working fine or not.

