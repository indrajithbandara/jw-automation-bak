#!/usr/bin/env python2.7
#coding: utf-8

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
#http://www.cnblogs.com/apexchu/p/4209742.html
#http://www.cnblogs.com/yangxia-test/category/431240.html

def send_mail():
    sender = 'jwlabusertester@163.com'
    receiver = 'jwlabusertester@163.com'
    subject = 'python email test'
    smtpserver = 'smtp.163.com'
    username = 'jwlabusertester@163.com'
    password = 'Passw0rd'

    msgRoot = MIMEMultipart('related')
    msgRoot['Subject'] = 'test message fuck'

    #构造附件
    test_report_dir='/var/lib/jenkins/workspace/test-Python/test-report/jwinterface_test_report.html'
    # test_report_dir='E:\\IDEidea\\IdeaProjects\\jw-automation\\test-report\\jwinterface_test_report.html'
    #'E:\\IDEidea\\IdeaProjects\\jw-automation\\test-report\\cwapi2016-11-10_12_28_34__test_report.html'
    att = MIMEText(open(test_report_dir, 'rb').read(), 'base64', 'utf-8')
    att["Content-Type"] = 'application/octet-stream'
    att["Content-Disposition"] = 'attachment; filename="jwinterface_test_report.html"'
    msgRoot.attach(att)
    try:
       smtp = smtplib.SMTP()
       smtp.connect('smtp.163.com')
       smtp.login(username, password)
       smtp.sendmail(sender, receiver, msgRoot.as_string())
       smtp.quit()
       print "send email is successful............."
       return True
    except Exception, e:
        #print str(e)
        return False


if __name__ == '__main__':
    send_mail()
