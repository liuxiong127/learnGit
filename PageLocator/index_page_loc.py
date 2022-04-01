# -*- encoding=utf8 -*- 
'''
@Time:  2021/4/15-17:14
@User:  Administrator
@File:  index_page_loc.py
@Email：  liuxiong@fcbox.com
'''

from selenium.webdriver.common.by import By
# 首页元素定位

class IndexPageLocator():

    gailan = (By.XPATH, '//span[text()="概览"]')
    system_manage = (By.XPATH, '//span[text()="系统管理"]')
    site_manage = (By.XPATH, '//span[text()="选址管理"]')