import smtplib

server=smtplib.SMTP_SSL("smtp.gmail.com",465)
server.login("shamolsheak@gmail.com","mahabub27dec1998!")
server.sendmail("shamolsheak@gmail.com",
                "mahabobur.piistech@gmail.com",
                "hello, guys")
server.quit()
