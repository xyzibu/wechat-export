#!/usr/bin/env python
# encoding: utf-8

import ConfigParser
from wxpy import *

import logging
import time
import smtplib
import time
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

logging.basicConfig(filename='/tmp/sendmail.log', level=logging.DEBUG)

cf = ConfigParser.ConfigParser()
cf.read('wechat.conf')

mail_host = cf.get('email', 'host')
mail_user = cf.get('email', 'user')
mail_pass = cf.get('email', 'pass')
mail_port = cf.get('email', 'port')
to = cf.get('email', 'to')
group_name = cf.get('wechat', 'group_name')
path = cf.get('wechat', 'path')

sender = mail_user
day = time.strftime("%Y-%m-%d")


def sendmail(receivers, message):
    smtpObj = smtplib.SMTP()
    smtpObj.connect(mail_host, mail_port)
    smtpObj.ehlo()
    smtpObj.starttls()
    smtpObj.login(mail_user, mail_pass)
    smtpObj.sendmail(sender, receivers, message.as_string())
    smtpObj.close()


def get_subject():
    subject = u'微信群[%s]聊天记录%s' % (group_name.decode('utf-8'), day)
    return subject

def get_message(subject):
    message = MIMEMultipart()
    message['Subject'] = Header(subject, 'utf-8')
    message['From'] = Header('<' + sender + '>', 'utf-8')

    file_name = ('%s.%s.txt' % (group_name, day))
    file_ab_path = os.path.join(path, file_name)
    if not os.path.exists(file_ab_path):
        logging.warning('%s is not existed!' % file_ab_path)
        return None

    att = MIMEText(open(file_ab_path,'rb').read(),'base64','utf-8')
    att["Content-Type"] = 'application/octet-stream'
    att["Content-Disposition"] = 'attachment; filename=%s' % (file_name)
    message.attach(att)
    return message

def main():
    receivers = to.split(' ')
    subject = get_subject()
    message = get_message(subject)
    if message is not None:
        logging.info(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        sendmail(receivers, message)


if __name__ == '__main__':
    main()
