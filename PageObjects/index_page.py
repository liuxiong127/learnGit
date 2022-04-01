# -*- encoding=utf8 -*- 
'''
@Time:  2021/4/15-17:19
@User:  Administrator
@File:  index_page.py
@Email：  liuxiong@fcbox.com
'''

from PageLocator.index_page_loc import IndexPageLocator
from Common.basepage import BasePage

class IndexPage(BasePage):
    # 点击进去选址管理
    def enter_siteManage(self):
        self.click_element(IndexPageLocator.site_manage, '点击选址管理按钮')

    def enter_gailan(self):
        self.click_element(IndexPageLocator.gailan, '点击概览按钮')


    def enter_systemManage(self):
        self.click_element(IndexPageLocator.system_manage, '点击系统管理')