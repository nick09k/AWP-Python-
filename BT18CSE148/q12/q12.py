# Schedule Library imported 
import schedule 
import time 
import smtplib, ssl
import random
 
	
def geeks(): 
    port = 587  # For starttls
    smtp_server = "smtp.gmail.com"
    sender_email = "nickpc007@gmail.com"
    reciever_email = ["asdfg@gmail.com","luffy@gmail.com","roronoazoro@gmail.com","blacklegsanji@gmail.com"]
    task=['dishes','cooking','vacuum','walk dog']
    password = input("Type your password and press enter:")

#context = ssl.create_default_context()
    for i in task:
        random_reciever=random.choice(reciever_email)
        random_task=random.choice(task)

        with smtplib.SMTP(smtp_server, port) as server:
            server.ehlo()  # Can be omitted
            server.starttls()
            server.ehlo()  # Can be omitted
            server.login(sender_email, password)
            server.sendmail(sender_email, random_reciever, random_task)

    task.remove(random_task)
    reciever_email.remove(random_reciever)
 

# Task scheduling 
# Every monday good_luck() is called 
schedule.every().monday.do(geeks) 
 
while True: 

	# Checks whether a scheduled task 
	# is pending to run or not 
	schedule.run_pending() 
	time.sleep(1) 
