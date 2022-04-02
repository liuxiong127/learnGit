# -*- encoding=utf8 -*- 
'''
@Time:  2021/4/20-16:13
@User:  Administrator
@File:  test2.py
@Email：  liuxiong@fcbox.com
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

dr = webdriver.Chrome()
dr.get("https://www.baidu.com/")
dr.maximize_window() #尺寸放到最大

WebDriverWait(dr,10, 0.5).until(EC.visibility_of_element_located((By.ID, "kw")))


dr.find_element(By.ID, "kw").send_keys("好123")
print(dr.title) #打印title
time.sleep(3) #停在界面上
dr.quit()