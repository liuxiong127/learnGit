# -*- encoding=utf8 -*- 
'''
@Time:  2021/4/15-16:40
@User:  Administrator
@File:  login_page_loc.py
@Email：  liuxiong@fcbox.com
'''

from selenium.webdriver.common.by import By

class LoginPageLocator():
    # 用户名输入框
    username = (By.ID, 'account')
    # 密码输入框
    password = (By.ID, 'password')
    # 验证码输入框
    verifyCode = (By.ID, 'verifyCode')
    # 登录按钮
    login_button = (By.ID, 'login')