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

#
# f1()
# index()
# goods()
for a in range(1,7,2):
    print(a)

b = range(1,8,2)
print(type(b),b[0])

def ranges(start,end,step):
    while start <end:
        yield start
        start+=step

c = ranges(1,7,2)
print(c.__next__())


