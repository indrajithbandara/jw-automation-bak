# -*- coding: UTF-8 -*-
import logging, time
import logging.handlers

rq = time.strftime('%Y%m%d', time.localtime(time.time()))
class LogUtils(object):
  '''日志类 '''
  def __init__(self, name):
       self.path = "../test-log/" # 定义日志存放路径
       self.filename = self.path + rq + '.log'    # 日志文件名称
       self.name = name    # 为%(name)s赋值
       self.logger = logging.getLogger(self.name)
        #控制日志文件中记录级别
       self.logger.setLevel(logging.INFO)
        #控制输出到控制台日志格式、级别
       self.ch = logging.StreamHandler()
       gs = logging.Formatter('%(asctime)s - %(levelname)s - %(name)s[line:%(lineno)d] - %(message)s')
       self.ch.setFormatter(gs)
      # self.ch.setLevel(logging.NOTSET)    写这个的目的是为了能控制控制台的日志输出级别，但是实际中不生效，不知道为啥，留着待解决
        #日志保留10天,一天保存一个文件
       self.fh = logging.handlers.TimedRotatingFileHandler(self.filename, 'D', 1, 10)
        #定义日志文件中格式
       self.formatter = logging.Formatter('%(asctime)s - %(levelname)s -   %(name)s[line:%(lineno)d] - %(message)s')
       self.fh.setFormatter(self.formatter)
       self.logger.addHandler(self.fh)
       self.logger.addHandler(self.ch)

 # class customError(Exception):
 # u'''    自定义异常类,用在主动输出异常时使用,用 raise关键字配合使用,例:
 #          if True:
 #                pass
 #          else:
 #                raise customError(msg)    '''
 #    def __init__(self, msg=None):
 #          self.msg = msg
 #    def __str__(self):
 #           if self.msg:
 #                  return self.msg
 #           else:
 #                  return u"某个不符合条件的语法出问题了"

# encoding:utf-8
import sys
import logging
import time
def writeLog(message):
     logger=logging.getLogger()
     filename = time.strftime('%Y-%m-%d',time.localtime(time.time()))
     handler=logging.FileHandler("../test-log/"+filename+"error")
     logger.addHandler(handler)
     logger.setLevel(logging.NOTSET)
     logger.info(message)
if __name__ == '__main__':
     writeLog("hello")
