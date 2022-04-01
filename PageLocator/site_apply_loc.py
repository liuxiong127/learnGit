# -*- encoding=utf8 -*- 
'''
@Time:  2021/4/15-17:25
@User:  Administrator
@File:  site_apply_page.py
@Email：  liuxiong@fcbox.com
'''

from selenium.webdriver.common.by import By

class SiteApplyLocator():
    # 选址申请按钮
    site_apply_button = (By.XPATH, '//div/img[@class="actionIcon___1NtR0 icon___3R3tu floatRight___3sicx"]')
    # 流程归属按钮
    flowBelong = (By.XPATH, '//label[contains(text(),"流程归属")]/parent::div/following-sibling::div')
    # 流程选择
    select_flow = (By.XPATH, '//*[contains(text(), "地区开发人员-广深")]')

    # 打开高德地图进行搜索
    gaode_map = (By.XPATH, '//a[text()="打开高德地图"]')
    search_input = (By.ID, 'pickerInput')
    select_address = (By.CSS_SELECTOR ,'li.sugg-item.sugg-no-id')
    select_poi = (By.CSS_SELECTOR, 'li.poibox')
    address_assure = (By.XPATH, '//button[text()="确定"]')