import smtplib
from email.mime.text import MIMEText
from email.header import Header

# �������������
smtpserver = "smtp.163.com"

# ���������û�������
user = "liangminyzu@163.com"
password = "SMGBEMLIVPESZPNB"

# ���ͺͽ�������
sender = "liangminyzu@163.com"
receive = "min.liang@gc.omron.com"

# �����ʼ����������
subject = "Web Selenium �Զ������Ա���"
content = "<html><h1 style='color:red'>�Զ������ԣ���ѧ�ɲ�</h1></html>"

# HTML�ʼ�����
msg = MIMEText(content, 'html', 'utf-8')
msg['Subject'] = Header(subject, 'utf-8')
msg['From'] = "liangminyzu@163.com"
msg['To'] = "min.liang@gc.omron.com"


# SSLЭ��˿ں�Ҫʹ��465
smtp = smtplib.SMTP_SSL(smtpserver, 465)

# HELO���������־�û����
smtp.helo(smtpserver)

# ���������ؽ��ȷ��
smtp.ehlo(smtpserver)

# ��¼����������û�������
smtp.login(user, password)

print("Send email start...")
smtp.sendmail(sender, receive, msg.as_string())
smtp.quit()
print("email send end!")







