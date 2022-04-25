# -*- encoding=utf8 -*- 
'''
@Time:  2022/4/21-9:46
@User:  Administrator
@File:  面向过程编程7.py
@Email：  liuxiong@fcbox.com
'''

'''
1、首先强调：面向过程编程绝对不是用函数编程这么简单，面向过程是一种编程思路、思想，而编程思路是不依赖于具体的语言或语法的。言外之意是即使我们不依赖于函数，也可以基于面向过程的思想编写程序

2、定义
面向过程的核心是过程二字，过程指的是解决问题的步骤，即先干什么再干什么

基于面向过程设计程序就好比在设计一条流水线，是一种机械式的思维方式

3、优点：复杂的问题流程化，进而简单化

4、缺点：可扩展性差，修改流水线的任意一个阶段，都会牵一发而动全身

5、应用：扩展性要求不高的场景，典型案例如linux内核，git，httpd

6、举例
流水线1：
用户输入用户名、密码--->用户验证--->欢迎界面

流水线2：
用户输入sql--->sql解析--->执行功能
'''

import re
def talk():
    users = get_user()
    print(users, type(users))
    while True:
        username = input("username-->>:").strip()
        if isNumLeters(username):
            if username in users:
                print("用户已存在！")
            else:
                break
        else:
            print("用户密码只能为字母数字下划线，且不能以数字开头")

    while True:
        passwd1 = input("输入密码-->:").strip()
        if len(passwd1)<8:
            print("密码过短")

        elif len(passwd1)>16:
            print("密码过长")
        else:
            passwd2 = input("确认密码-->:").strip()
            if passwd1 == passwd2:
                break
            else:
                print("两次输入的密码不一致！！")


    role_dict = {
        "1":"user",
        '2':"admin"
    }

    while True:
        for k in role_dict:
            print(k,role_dict[k])
        choice = input('请输入您的身份>>: ').strip()
        if choice not in role_dict:
            print('输入的身份不存在')
            continue
        else:

            role1 = role_dict[choice]
            break
    return username,passwd1,role1



def get_user():
    with open('../datas/user.txt', encoding="utf-8") as f:
        res = f.readlines()
        user = []
        for i in res:
            user.append(i.split(":")[0])
    return user



def isNumLeters(s):
    s = str(s)
    if s == '':
        return False
    if len(s)<2:
        if re.match('^[a-zA-Z_]+$',s[0]):
            return True
        else:
            return False
    else:
       if re.match('^[a-zA-Z_]+$', s[0]) and re.match('^[0-9a-zA-Z_]+$',s[1:]):
            return True
       else:
           return False




def register_interface(username,password,role):
    format_str = "%s:%s:%s\n"%(username, password, role)
    return format_str

def handle_file(format_str,filepath):
    with open(r'%s' %filepath,'at',encoding='utf-8') as f:
        f.write(format_str)

def register():
    user,pwd,role=talk()
    format_str=register_interface(user,pwd,role)
    handle_file(format_str,'../datas/user.txt')


register()
# get_user()