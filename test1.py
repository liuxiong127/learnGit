# -*- encoding=utf8 -*- 
'''
@Time:  2022/4/1-11:13
@User:  Administrator
@File:  test1.py.py
@Email：  liuxiong@fcbox.com
'''

from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
time.sleep(5)
driver.maximize_window()
time.sleep(2)
driver.close()



