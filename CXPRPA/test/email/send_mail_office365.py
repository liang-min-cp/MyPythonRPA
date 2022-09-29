import emails
from emails.template import JinjaTemplate as T


USERNAME = 'min.liang@gc.omron.com'
PASSWORD = 'Oms=2022'
smtp_conf = {'host': 'smtp.office365.com',
             'user': USERNAME,
             'password': PASSWORD,
             'port': 587,
             'tls': True}


def send_email():
    message = emails.html(subject=T('测试邮件'),
                          html=T('<p>详情见附件<br><br>'),
                          mail_from=('auto-reporter', USERNAME))
    # message.attach(data=open('readme.md', 'r'), filename="readme.txt")
    r = message.send(to=('Orangleliu', "liangminyzu@163.com"), smtp=smtp_conf)
    print(r)


def office365():
    import smtplib
    mailserver = smtplib.SMTP('smtp.office365.com', 587)
    mailserver.ehlo()
    mailserver.starttls()
    mailserver.login(USERNAME, PASSWORD)
    mailserver.sendmail(USERNAME, USERNAME, 'python email')
    mailserver.quit()


if __name__ == "__main__":
    send_email()




