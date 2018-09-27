#!/usr/bin/python3

import os
import datetime
import subprocess as sp
import smtplib
from sys import argv

time = str(datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S'))

def send_mail():
    log_msg = argv[1]
    mail_srv = 'mail.novusgroup.co.za'
    mail_port = '25'
    mail_name = 'server@novusgroup.co.za'
    mail_recip = ['michael@novusgroup.co.za']
    mail_sub = 'Server notification'
    mail_msg = 'Subject: {}\n\n{}'.format(mail_sub, log_msg)
    smtpServ = smtplib.SMTP(mail_srv, mail_port)
    smtpServ.sendmail(mail_name, mail_recip, mail_msg)
    smtpServ.quit()
    print('Sending email notification to: %s' % mail_recip)


if __name__ == '__main__':
    send_mail()
