# -*- encoding=utf8 -*- 
'''
@Time:  2019/10/23-13:36
@User:  Administrator
@File:  project_path.py
@Email：  liuxiong@fcbox.com
'''

import os

'''
动态获取相关路径
'''

# 项目根路径
project_path = os.path.dirname(os.path.dirname(__file__))

# 截图存放路径
screenshots_path = os.path.join(project_path,'Outputs','screenshots')

# 测试报告存放路径
test_report_path = os.path.join(project_path,'Outputs','reports','test_report.html')

# 日志存放路径
test_log_path = os.path.join(project_path,'Outputs','logs')

# 上传所用的附件存放路径
upload_file_path = os.path.join(project_path,'TestDatas')

