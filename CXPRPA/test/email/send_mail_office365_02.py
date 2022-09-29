import smtplib
from email.message import EmailMessage

# Define smtp.office365.com which is the SMTP Server for Office 365 with username & password
user = "10033230C6A01CA1"
password = 'Oms=2022'
smtpsrv = "smtp.office365.com"
smtpserver = smtplib.SMTP(smtpsrv, 587)

# Define the sender, receiver, and subject

msg = EmailMessage()

msg['Subject'] = 'Email Testing with Python'
msg['From'] = 'min.liang@gc.omron.com'
msg['To'] = 'liangminyzu@163.com'

smtpserver.ehlo()
smtpserver.starttls()
smtpserver.login(user, password)
smtpserver.send_message(msg)
smtpserver.close()



