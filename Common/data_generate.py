# -*- encoding=utf8 -*- 
'''
@Time:  2019/12/13-10:06
@User:  Administrator
@File:  data_generate.py
@Email：  liuxiong@fcbox.com
'''


import string
import random

class CommonFunction():

    def get_letter(self):
        '''
        随机获取一个字母
        :return:
        '''
        s = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        return random.choice(s)


    def get_double_number(self, n):
        '''
        随机获取一个两位数的字符串
        :return: > 返回一个两位数的字符串
        '''
        num = string.digits
        strs = ''
        for i in range(n):
            strs = strs + random.choice(num)
        return strs


    def get_chinese_charactor(self):
        val = "测试标准定制线"
        return random.choice(val)

