# -*- encoding=utf8 -*- 
'''
@Time:  2022/4/20-15:07
@User:  Administrator
@File:  名称空间与作用域3.py
@Email：  liuxiong@fcbox.com
'''
'''
一 什么是名称空间？

#名称空间：存放名字的地方，三种名称空间，
（之前遗留的问题x=1，1存放于内存中，那名字x存放在哪里呢？名称空间正是存放名字x与1绑定关系

二 名称空间的加载顺序

python test.py
#1、python解释器先启动，因而首先加载的是：内置名称空间
#2、执行test.py文件，然后以文件为基础，加载全局名称空间
#3、在执行文件的过程中如果调用函数，则临时产生局部名称空间


三 名字的查找顺序

复制代码
局部名称空间--->全局名称空间--->内置名称空间

#需要注意的是：在全局无法查看局部的，在局部可以查看全局的，如下示例

'''

# max1=1
# def f1():
#     # max1=2
#     def f2():
#         # max1=3
#         print(max1)
#     f2()
# f1()
# print(max1)


'''
四 作用域

#1、作用域即范围
        - 全局范围（内置名称空间与全局名称空间属于该范围）：全局存活，全局有效
        - 局部范围（局部名称空间属于该范围）：临时存活，局部有效
#2、作用域关系是在函数定义阶段就已经固定的，与函数的调用位置无关

#3、查看作用域：globals(),locals()


LEGB 代表名字查找顺序: locals -> enclosing function -> globals -> __builtins__
locals 是函数内的名字空间，包括局部变量和形参
enclosing 外部嵌套函数的名字空间（闭包中常见）
globals 全局变量，函数定义所在模块的名字空间
builtins 内置模块的名字空间

五、 global与nonlocal关键字

'''

# x=1
# def f1():
#     def f2():
#         print(x)
#     return f2
# # x=100
# def f3(func):
#     x=2
#     func()
# x=10000

# f3(f1())

name = "shangsan"
def change_name():
    name = "chenpei"
    print("change_name", name)


def change_name1():
    global name
    name = "chenpei"
    print("change_name", name)


def changes():
    test = "shanyizhonggong"
    print(test)

change_name()
change_name1()
print(name)

