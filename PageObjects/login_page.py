# -*- encoding=utf8 -*- 
'''
@Time:  2021/4/15-16:38
@User:  Administrator
@File:  login_page.py
@Email：  liuxiong@fcbox.com
'''
from PageLocator.login_page_loc import LoginPageLocator
from Common.basepage import BasePage

class LoginPage(BasePage):
    def login(self,username, passwd, code):
        self.input_text(LoginPageLocator.username, "输入用户名",username)
        self.input_text(LoginPageLocator.password, "输入密码", passwd)
        self.input_text(LoginPageLocator.verifyCode, "输入验证码", code)
        self.click_element(LoginPageLocator.login_button, '点击登录按钮')

