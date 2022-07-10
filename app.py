import smtplib
import sys
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import datetime
from apscheduler.schedulers.background import BackgroundScheduler
import schedule
import time

def reminder_mail():
    print("Sending mail")
    with open("D:/OneLearn.io/schedule.txt", "r") as sch:
        for content in sch:
            body = content.split("-")
            today_date = datetime.datetime.today()
            format = "%Y %d %b %H:%M %p"
            class_date = datetime.datetime.strptime(body[0].strip(), format)
            print(class_date)
            if class_date.weekday() in [1, 2, 3, 4]:
                if class_date.date() - today_date.date() == datetime.timedelta(days= 1):
                    #The mail address and password
                    mail_content = "This is a reminder mail for your class on" + body[1] + " at "+body[0].strip()+". " +" Pls join the class on time." 
                    sender_address = sys.argv[1]
                    sender_pass = sys.argv[2]
                    receiver_address = sys.argv[3]
                    #Stup the MIME
                    message = MIMEMultipart()
                    message["From"] = sender_address
                    message["To"] = receiver_address
                    message["Subject"] = "OneLearn course series reminder"
                    #The body and the attachments for the mail
                    message.attach(MIMEText(mail_content, "plain"))
                    #Create SMTP session for sending the mail
                    session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
                    session.starttls() #enable security
                    session.login(sender_address, sender_pass) #login with mail_id and password
                    text = message.as_string()
                    session.sendmail(sender_address, receiver_address, text)
                    session.quit()
                    print('Mail Sent')
                else:
                    continue
            
            elif class_date.date() - today_date.date() == datetime.timedelta(days = 3):
                #The mail address and password
                mail_content = "This is a reminder mail for your class on" + body[1] + " at "+body[0].strip()+". " +" Pls join the class on time." 
                sender_address = sys.argv[1] #"chandu23899@gmail.com" 
                sender_pass = sys.argv[2] #"#Chandu23"
                receiver_address = sys.argv[3] #"nakkapraneeth23899@gmail.com" 
                #Stup the MIME
                message = MIMEMultipart()
                message["From"] = sender_address
                message["To"] = receiver_address
                message["Subject"] = "OneLearn course series reminder"
                #The body and the attachments for the mail
                message.attach(MIMEText(mail_content, "plain"))
                #Create SMTP session for sending the mail
                session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
                session.starttls() #enable security
                session.login(sender_address, sender_pass) #login with mail_id and password
                text = message.as_string()
                session.sendmail(sender_address, receiver_address, text)
                session.quit()
                print('Mail Sent')
            else:
                continue
def p():
    print("hello")
# sched = BackgroundScheduler(daemon=True)
# sched.add_job(reminder_mail,'cron',)
if __name__ == '__main__':
#    schedule.every().day.at("10:25").do(reminder_mail)
    #  schedule.every().day.at("00:00").do(reminder_mail)
    sched = BackgroundScheduler(timezone='Asia/Kolkata')
    sched.add_job(p,'cron', second="10")
    sched.start()

    # try:
    #     # This is here to simulate application activity (which keeps the main thread alive).
    #     # while True:
    #     #     time.sleep(5)
    # except (KeyboardInterrupt, SystemExit):
    #     # Not strictly necessary if daemonic mode is enabled but should be done if possible
    #     sched.shutdown()

    
while True:
    sched.run_pending()
    time.sleep(1)
