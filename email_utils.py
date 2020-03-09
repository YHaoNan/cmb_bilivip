#!/usr/bin/env python
# coding=utf-8

import smtplib
from email.mime.text import MIMEText
from email.header import Header
import config as cfg


smtpObj = None
def init():
    print("Init email system...")
    try:
        global smtpObj
        smtpObj = smtplib.SMTP_SSL(cfg.SMTP_SERVER,cfg.SMTP_PORT)
        smtpObj.login(cfg.SENDER_ACCOUNT,cfg.SENDER_TOKEN)
        return True
    except Exception as err:
        print(err)
        return False

def send_email(msg):
    if smtpObj == None:
        print("[-] Please call email_utils.init() before you send email!!")
        return
    try:
        message = MIMEText(msg,"plain","utf-8")
        message["From"] = Header(cfg.SENDER_UNAME,"utf-8")
        message["To"] = Header("Reciver","utf-8")
        subject = "Bilibili大会员监听服务"
        message['Subject'] = Header(subject,"utf-8")
        smtpObj.sendmail(cfg.SENDER_ACCOUNT,cfg.RECIVER_ACCOUNTS,message.as_string())
        print("[+] 邮件发送成功")
    except Exception as e:
        print("[-] 邮件发送失败，%s"%e)
