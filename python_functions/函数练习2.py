# -*- encoding=utf8 -*- 
'''
@Time:  2022/4/20-16:19
@User:  Administrator
@File:  函数练习2.py
@Email：  liuxiong@fcbox.com
'''


login_status = {"user":None, "status":False}

def auth(func):
    def wapper(*args, **kwargs):
        if login_status['status']:
            return func(*args, **kwargs)
        else:
            user = input("user->>:")
            passwd = input("password->>:")
            with open('../datas/db.txt', encoding="utf-8") as f:
                res = eval(f.read())
            if user==res['user'] and passwd == res['passwd']:
                login_status['user'] = user
                login_status['status'] = True
                print("login success！！")
                res = func(*args, **kwargs)
                return res
            else:
                print("login 失败!!")
    return wapper
@auth
def f1():
    print("访问主页")

@auth
def index():
    print("进去好不好")
    print("zhe buhao ba ")
    print("laizhebushan")


@auth
def goods():
    print("购物车满了")


f1()
index()
goods()


