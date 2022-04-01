# -*- encoding=utf8 -*- 
'''
@Time:  2019/10/23-13:47
@User:  Administrator
@File:  logger.py
@Email：  liuxiong@fcbox.com
'''

'''
日志输出设置
'''

import logging
from logging.handlers import  RotatingFileHandler
import time
from Common import project_path

fmt = " %(asctime)s  %(levelname)s %(filename)s %(funcName)s [ line:%(lineno)d ] %(message)s"
datefmt = '%a, %d %b %Y %H:%M:%S'

handler_1 = logging.StreamHandler()

curTime = time.strftime("%Y-%m-%d-%H%M", time.localtime())

handler_2 = RotatingFileHandler(project_path.test_log_path+"/Web_Autotest_{0}.log".format(curTime),backupCount=20,encoding='utf-8')

#设置rootlogger 的输出内容形式，输出渠道
logging.basicConfig(format=fmt,datefmt=datefmt,level=logging.INFO,handlers=[handler_1,handler_2])

# logging.info("hehehe")