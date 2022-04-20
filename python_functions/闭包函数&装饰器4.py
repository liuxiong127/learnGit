# -*- encoding=utf8 -*- 
'''
@Time:  2022/4/20-15:20
@User:  Administrator
@File:  闭包函数&装饰器4.py
@Email：  liuxiong@fcbox.com
'''
'''
一 什么是闭包？

复制代码
#内部函数包含对外部作用域而非全局作用域的引用

#提示：之前我们都是通过参数将外部的值传给函数，闭包提供了另外一种思路，包起来喽，包起呦，包起来哇
'''

# def counter():
#     n=0
#     def incr():
#         nonlocal n
#         x=n
#         n+=1
#         return x
#     return incr
#
# c=counter()
# print(c())
# print(c())
# print(c())
# print(c())
# print(c())
# print(c.__closure__[0].cell_contents) #查看闭包的元素

'''
二 闭包的意义与应用

复制代码
#闭包的意义：返回的函数对象，不仅仅是一个函数对象，在该函数外还包裹了一层作用域，
这使得，该函数无论在何处调用，优先使用自己外层包裹的作用域
#应用领域：延迟计算（原来我们是传参，现在我们是包起来）
'''
# from urllib.request import urlopen
#
# def index(url):
#     def get():
#         return urlopen(url).read()
#     return get
#
# baidu=index('https://www.baidu.com')
# print(baidu().decode('utf-8'))

'''
五 装饰器
装饰器就是闭包函数的一种应用场景

一 为何要用装饰器

#开放封闭原则：对修改封闭，对扩展开放

二 什么是装饰器

装饰器他人的器具，本身可以是任意可调用对象，被装饰者也可以是任意可调用对象。
强调装饰器的原则：1 不修改被装饰对象的源代码 2 不修改被装饰对象的调用方式
装饰器的目标：在遵循1和2的前提下，为被装饰对象添加上新功能
'''

# 无参装饰

# import time
# def timer(func):
#     def wapper(*args, **kwargs):
#         start = time.time()
#         res = func(*args, **kwargs)
#         end = time.time()
#         print("耗费时间%s"%(end-start))
#         return res
#     return wapper
#
# @timer
# def foo(n):
#     time.sleep(2)
#     for i in range(n):
#         # print("{0}*{1}={2}".format(i,i,i*i))
#         if i+1==n:
#             return i*i
#
#
#
# res = foo(10000000)
# print(res)

# 有参装饰

# def login(driver='file'):
#     def auth(func):
#         def wapper(*args, **kwargs):
#             user = input("user->>:")
#             passwd = input("passwd->>:")
#             if driver=="file":
#                 if user=="admin" and passwd=="123456":
#                     print("login success!!")
#                     return func(*args, **kwargs)
#                 else:
#                     print("用户名或密码错误")
#             elif driver=="lapd":
#                 print("lapd")
#             else:
#                 print("login 失败！！")
#         return wapper
#     return auth

# @timer
# @login(driver='file')
# def calc1(x,y,z):
#     time.sleep(0.5)
#     return x+y+z
# res1 = calc1(3,6,9)
# print(res1)
#
# @login(driver='files')
# def calc2():
#     print("123")
# calc2()


'''
四 装饰器语法

复制代码
被装饰函数的正上方，单独一行
        @deco1
        @deco2
        @deco3
        def foo():
            pass

        foo=deco1(deco2(deco3(foo)))

'''

'''
五 装饰器补充：wraps
'''
# from functools import wraps
#
# def deco(func):
#     @wraps(func) #加在最内层函数正上方
#     def wrapper(*args,**kwargs):
#         return func(*args,**kwargs)
#     return wrapper

# @deco
# def index():
#     #哈哈哈哈
#     print('from index')
#
# index()
# print(index.__doc__)


'''
六 叠加多个装饰器

# 叠加多个装饰器
# 1. 加载顺序(outter函数的调用顺序):自下而上
# 2. 执行顺序(wrapper函数的执行顺序):自上而下
'''
import time

def outter1(func):
    print("加载outter1……")
    def wapper1(*args, **kwargs):
        print("执行中outter1")
        return func(*args, **kwargs)
    return wapper1

def outter2(func):
    print("加载outter2……")
    def wapper2(*args, **kwargs):
        print("执行中outter2")
        return func(*args, **kwargs)
    return wapper2


def outter3(func):
    print("加载outter3……")
    def wapper3(*args, **kwargs):
        print("执行中outter3")
        return func(*args, **kwargs)
    return wapper3

@outter1
@outter2
@outter3
def test(x,y,z):
    time.sleep(0.5)
    return x+y+z


test(3,6,5)