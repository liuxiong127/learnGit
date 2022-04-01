# -*- encoding=utf8 -*- 
'''
@Time:  2019/10/29-11:45
@User:  Administrator
@File:  conftest.py
@Email：  liuxiong@fcbox.com
'''
from selenium import webdriver
from TestDatas import common_datas as cd
import pytest
from PageObjects.login_page import LoginPage

"""
conftest.py 前置后置共享文件，可以不用主动去调用，相比unittest更优 使用@pytest.fixture
"""

@pytest.fixture()
def init_driver():
    # 前置
    driver = webdriver.Chrome()
    driver.get(cd.web_url)
    driver.maximize_window()
    # 区分前置后置，并返回
    yield driver
    # 后置
    driver.quit()

@pytest.fixture()
def login_driver():
    # 前置
    LoginPage(init_driver).login(cd.user, cd.password, cd.code)
    yield init_driver # 返回

@pytest.fixture()
def test():
    # 前置
    print("这是一个测试用例前置，测试前准备")
    yield True
    # 后置
    print("这是一个测试用例后置，测试后恢复环境")
