from smtplib import SMTP_SSL as SMTP
import smtplib
from email.mime.multipart import  MIMEMultipart
from email.mime.text import MIMEText
import os.path


class Email(object):
    def __init__(self):
        self.sender = "noreply@keerthan.com"
        self.password = "keerthan"

    def send_mail(self,recevier,subject,message,attachment = [],cc=None,is_credential= True):
        server = SMTP("mail.aparajitha.com",587)
        server.set_debuglevel(False)
        server.login(self.sender,self.password)
        msg = MIMEMultipart()
        msg['From'] = self.sender
        msg['To'] = ",".join(recevier) if type(recevier) is list else recevier
        msg['Subject'] = subject
        if cc is not None:
            msg['Cc'] = ",".join(cc)
        msg.attach(MIMEText(message, 'html'))
        final_receiver = recevier
        for f in attachment:
            with open(f,'rb') as a_file:
                basename = os.path.basename(f)
                part = MIMEApplication(a_file.read(),Name=basename)
            part['Content-Disposition'] = 'attachement;filename="%s"'%basename
            msg.attach(part)
        if cc is not None:
            if type(cc) is list:
                final_receiver = recevier + cc if (type(recevier) is list) else cc + [recevier]
            else:
                final_receiver = recevier +[cc] if (type(recevier) is list) else [recevier] +[cc]
        response = server.sendmail(self.sender,final_receiver,msg.as_string())
        print(response)
        server.close()
