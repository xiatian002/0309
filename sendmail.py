# -*- coding:utf-8 -*- 
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
HOST="smtp.126.com"
TITLE="Send python file"
TO="zhangpeng@conac.cn"
FROM_ADDR="zhang_peng101@126.com"
CONTENT=MIMEText("Send text again.This time send a attach!")#邮件格式的纯文本，邮件中的内容部分
#BODY="\r\n".join((
 #   "From: %s" % FROM_ADDR,
 #   "TO: %s" % TO,
 #   "Subject: %s" %TITLE,
 #   "",
 #   CONTENT
#))
attact=MIMEText(open("sla.py","rb").read(),"base64","utf-8")
#attact["Content-Type"]="application/octet-stream"
attact.add_header('Content-Disposition','attactment',filename='sla.py')
msg=MIMEMultipart('related')#创建邮件对象。
msg.attach(attact)
msg.attach(CONTENT)
msg['Subject'] = TITLE
msg['From']=FROM_ADDR
msg['To']=TO
server=smtplib.SMTP()
server.connect(HOST,"25")
server.starttls()
server.login("zhang_peng101@126.com","xxxxxx")
server.sendmail(FROM_ADDR,TO,msg.as_string())
server.quit()
