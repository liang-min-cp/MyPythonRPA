import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart

# 发送邮箱服务器
smtpserver = "smtp.163.com"

# 发送邮箱用户名密码
user = "liangminyzu@163.com"
password = "SMGBEMLIVPESZPNB"

# 发送和接收邮箱
sender = "liangminyzu@163.com"
receive = "min.liang@gc.omron.com"

# 发送邮件主题和内容
subject = "Web Selenium 自动化测试报告"
content = "<html><h1 style='color:red'>自动化测试，自学成才</h1></html>"

# HTML邮件正文
msg = MIMEText(content, 'html', 'utf-8')
msg['Subject'] = Header(subject, 'utf-8')
msg['From'] = "liangminyzu@163.com"
msg['To'] = "min.liang@gc.omron.com"


# 附件

# ...
send_file = open(r"test.txt", "rb").read()

att = MIMEText(send_file, "base64", 'utf-8')
att['Content-Type'] = 'application/octet-stream'
att['Content-Disposition'] = 'attachment;filename="test.txt"'

msgRoot = MIMEMultipart()
msgRoot.attach(MIMEText(content, 'html', 'utf-8'))
msgRoot['Subject'] = subject
msgRoot['From'] = sender
# msgRoot['To'] = ','.join(receives)
msgRoot['To'] = receive
msgRoot.attach(att)
#...



# SSL协议端口号要使用465
smtp = smtplib.SMTP_SSL(smtpserver, 465)

# HELO向服务器标志用户身份
smtp.helo(smtpserver)

# 服务器返回结果确认
smtp.ehlo(smtpserver)

# 登录邮箱服务器用户名密码
smtp.login(user, password)

print("Send email start...")
# smtp.sendmail(sender, receive, msg.as_string())
smtp.sendmail(sender, receive, msgRoot.as_string())
smtp.quit()
print("email send end!")







