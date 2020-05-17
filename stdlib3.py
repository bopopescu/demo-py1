import smtplib

server = smtplib.SMTP_SSL('smtp.gmail.com',465)
server.ehlo()
server.login('gmail_user','ur_password')
server.sendmail('gmail_user','to_gmail_user','hello test email')
server.close()
print("Email is sent.")
