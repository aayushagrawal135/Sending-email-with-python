#send an E-mail with a python script
#From g-mail Go to 'Allow less secure apps to access my account' setting, and turn it On

#smtp : Simple Mail Tranfer Protocol, a library to use its functionality
import smtplib

#Libraries needed to part the content as subject, body of the mail
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

#Sender email, receiver email (receiver email could be a list of email addresses as well)
sender = "CCCCCCCC@gmail.com"
sender_password = "BBBBBBBB"
receiver = "AAAAA@gmail.com"

#Subject and body of the mail
subject = "something"
body = "waiting eagerly for a mail!"

msg = MIMEMultipart()
msg["From"] = sender
msg["To"] = receiver
msg["Subject"] = subject

structure = MIMEText(body, 'plain')
msg.attach(structure)

final_message = msg.as_string()

#parameters: hostname/server IP, port number : Look up for the port number corresponding to hostname you use
try:
	server = smtplib.SMTP("smtp.gmail.com", 587)
except Error:
	print("Connection Unsuccessful")
else:
	print("Connection successful")

#Enables for encrypted communication with the smtp servers
server.starttls()

try:
	server.login(sender, sender_password)
	server.sendmail(sender, receiver, final_message)
except Error:
	print(Error)
else:
	print("Mail successfully sent")

server.quit()
