# question 13
#I have enabled two step verification in gamil so login failed.... 

import smtplib #importing smtp library 
s = smtplib.SMTP('smtp.gmail.com', 587) # createing SMTP session using port number given
s.starttls()# starting  TLS for security to encrypt all smtp command  
s.login("sender_email_id", "sender_email_id_password")## Login  Authentication for sender eamil id and password   
message = "This is for python asignment " # message to be sent
s.sendmail("sender_email_id", "receiver_email_id", message) # syntax to send mail request
s.quit() # terminating the session 
