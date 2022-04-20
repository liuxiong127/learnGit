
# -*- encoding=utf8 -*-
'''
@Time:  2022/4/20-14:43
@User:  Administrator
@File:  函数对象.py
@Email：  liuxiong@fcbox.com
'''

def foo():
    print("选择对了……")
    print("foo")

def bar():
    print("bar")



dic={
    'foo':foo,
    'bar':bar,
}
while True:
    choice=input('>>: ').strip()
    if choice in dic:
        dic[choice]()