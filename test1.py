# -*- encoding=utf8 -*- 
'''
@Time:  2022/4/1-11:13
@User:  Administrator
@File:  test1.py.py
@Email：  liuxiong@fcbox.com
'''

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get("http://cns-sit5.fcbox.com")

locator = (By.ID, 'userValidateTitle')
WebDriverWait(10, 0.1, driver).until(EC.visibility_of_element_located(locator))
driver.maximize_window()
time.sleep(5)

driver.find_element(By.ID, 'account').send_keys("003398")



