import smtplib

sender = 'your_mail.com'
receiver = ['email1','email2','email3'...]
message = """\
Subject: test

this is just a test with using smtp protocol to send mails """

server = smtplib.SMTP('smtp.gmail.com', 587) #this line is fix is for the port and the protocol info
server.starttls() #protect your msg
server.login(sender, "gmail_password_app") #serch in youtube how you can get it
server.sendmail(sender, receiver, message)
print("email has been send seccusfly")