import smtplib, ssl

port = 465

sender='shamolsheak@gmail.com'
password = 'mahabub27dec1998!'

recieve = 'mahabobur.piistech@gmail.com','foysal.piistech@gmail.com','ahmediftekhar735@gmail.com','jannatulmahi23@gmail.com'

message = """\
Subject: Automatic send mail

hi, i am mahabub.

thanks
"""

context = ssl.create_default_context()

print("Starting to send")
with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    server.login(sender, password)
    server.sendmail(sender, recieve, message)

print("sent email!")
