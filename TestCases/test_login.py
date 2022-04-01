# -*- encoding=utf8 -*- 
'''
@Time:  2021/4/15-17:01
@User:  Administrator
@File:  test_login.py
@Email：  liuxiong@fcbox.com
'''

import pytest
import time
from selenium import webdriver
from PageObjects.login_page import LoginPage
from TestDatas import common_datas as cd
from PageObjects.index_page import IndexPage
from PageObjects.site_page import SitePage
#
# @pytest.mark.usefixtures('init_driver')
# class TestLogin():
#     def test_login_success(self, init_driver):
#         LoginPage(init_driver).login(cd.user, cd.password, cd.code)
#         time.sleep(5)
#         IndexPage(init_driver).enter_siteManage()
#         SitePage(init_driver).add_site_apply()

@pytest.mark.usefixtures('login_driver')
class TestLogin1():
    def test_login(self, login_driver):
        time.sleep(5)
        IndexPage(login_driver).enter_siteManage()
        SitePage(login_driver).add_site_apply()