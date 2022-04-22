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

def talk():
    while True:
        username = input("username-->>:").strip()
        if username.isalpha():
            break
        else:
            print("用户密码只能为字母")


    while True:
        passwd1 = input("输入密码-->:").strip()
        passwd2 = input("确认密码-->:").strip()
        if passwd1 == passwd2:
            break
        else:
            print("两次输入的密码不一致！！")
    return username,passwd1


def register_interface(username,password):
    format_str = "%s:%s"%(username, password)
    return format_str