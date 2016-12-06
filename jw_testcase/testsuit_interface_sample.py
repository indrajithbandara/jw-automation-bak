# -*- coding: utf-8 -*-
#encoding:utf-8
import unittest, time, re
import HTMLTestRunner
import generateutils
import os
import shutil
from  jw_utils import connection_db



if __name__ == '__main__':
    suite = unittest.TestSuite()
    #suite.addTest(get_order_list('test_get_order_list'))
    #suite.addTest(testcase_api_account_login('test_testcase_api_account_login'))
    #suite.addTest(testcase_api_account_login('test_testcase_api_account_changeuser'))
    #suite.addTest(testcase_api_account_login('test_testcase_api_account_changepassword'))
    #suite.addTest(testcase_api_account_login('test_testcase_api_account_changeacl'))
    #outfile=open("c://edaixi_testdata//report.html",'wb')
    #filename = 'G:\\seleniums\\result.html'
    connection_db.select();
    generateutils.httpGetImplement("assertgetdemo1111");
    generateutils.httpPostSendImplement("assertgetdemo333");
    #generateutils.httpPostImplement("assertpostdemo111");
    # discover
    # discover = suite.defaultTestLoader.discover("D:\\PycharmProjects\\cloudwisdom_automation\\jw_testcase",
    #                                                pattern='*Implement.py',
    #                                                top_level_dir=None)
    # for suite in discover:
    #     for test_case in suite:
    #         suite.addTests(test_case)
    #         print suite
    #windows dir path
    test_dir="E:\\IDEidea\\IdeaProjects\\jw-automation\\jw_testcase"
    test_report_dir="E:\\IDEidea\\IdeaProjects\\jw-automation\\test-report\\"

    #linux redhat7 dir path
    #test_dir="/var/lib/jenkins/workspace/test-Python/jw_testcase"
    #test_report_dir="/var/lib/jenkins/workspace/test-Python/test-report/"

    discover = unittest.defaultTestLoader.discover(test_dir, pattern='*Impl.py')
    currenttime=time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())
    print currenttime
    #fp = file("/usr/edaixi_report/"+currenttime+"caiwu_test_report.html", 'wb')
    nowtime = time.strftime('%Y-%m-%d_%H_%M_%S_')
    fp = file(test_report_dir+"cwapi"+nowtime+"_test_report.html", 'wb')
    #fp = file("c:\\edaixi_testdata\\20150717caiwu_test_report.html", 'wb')

    htmlRunner= HTMLTestRunner.HTMLTestRunner(stream=fp,title=u'CloudWisdomInterface测试报告',description=u"用例执行情况 by 201611 softwareluke")
    #suite =  unittest.TestLoader().loadTestsFromTestCase(MyTest)
    htmlRunner.run(discover)
    fp.close()
