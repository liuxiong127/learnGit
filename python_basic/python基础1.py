# -*- encoding=utf8 -*- 
'''
@Time:  2022/4/2-11:41
@User:  Administrator
@File:  python基础1.py
@Email：  liuxiong@fcbox.com
'''


# python基础知识
'''
python注释
'''



'''
数据类型
数值
字符串
列表
元组
字典
集合
'''

# 数值
'''
整数  int
浮点数 float
复数 complex

int() 将字符串转换为数值
bit_length() 用二进制表示所需要的最少位数
'''
# num1 = 23
# num2 = 34.56
# num3 = 4+5j
# print(num1, type(num1))
# print(num2, type(num2))
# print(num3, type(num3))
#
#
# print(num1.bit_length())
#
# str1 = "123"
# str2 = "34.67"
# str3 = "4-6j"
# n1 = int(str1)
# n2 = float(str2)
# n3 = complex(str3)
# print(n1, type(n2))
# print(n2, type(n2))
# print(n3, type(n3))


'''
字符串的 
标识：str


'''

# 字符串的表示方法
# str1 = "abcdefg"
# str2 = '123123好的'
# str3 = '''测试员真的好不好'''
#
# print(str1, str2, str3)

# capitalize() 首字母大写，其余变小写
# v = "alex MKike"
# print(v.capitalize())
# casefold()变成小写
# print(v.casefold())
#
# print(v.center(50, '*'))
# print(v.count('e',1,10))
#
# print(v.endswith('ke'))
# print(v.startswith('al'))
#
# v = "alex123123123\thaode\t123"
# print(v.expandtabs())

# v = "abcdef"
# find() 查找子字符串是否存在，存在返回下标，不存在返回-1
# print(v.find('c'))
# print(v.find('dd'))

## 字符串的格式化操作
# v = "name:{name} age:{age}".format(name="mike", age=45)
# v1 = "name:{} age:{}".format("mike", 45)
#
# print(v)
# print(v1)
# v2 = "name:{name} age:{age}".format_map({"name":"mike", "age":56})
# print(v2)


# 查看子字符串的索引，找到就返回索引，找不到就报错
# v = "gjhgsjgf"
# print(v.index('h'))
#
# v1 = "123aghgjsdhjAAADF"
# v2 = "123"
# v3 = "ahjghjd"
# v4 = "--hjkgs123"
# print(v1.isalnum())
# print(v2.isalnum())
# print(v3.isalnum())
# print(v4.isalnum())

# isalpha() 判断字符串是否为字母
# v1 = "aghgjsdhjAAADF"
# v2 = "123"
# v3 = "ahjghjd234"
# v4 = "--hjkgs123"
# print(v1.isalpha())
# print(v2.isalpha())
# print(v3.isalpha())
# print(v4.isalpha())


# 判断是否是ASCII码
# v1 = "0101233459!@#!@#<>?"
# print(v1.isascii())


# isdecimal() 判断字符串是否为10进制整数
# isdigit() 判断字符串是否为数字字符串

# v1 = "12.34"
# v2 = "12"
# print(v1.isdecimal())
# print(v2.isdecimal())

# v1 = "23"
# v2 = "23.45"
# print(v2.isdigit())


# isidentifier()  判断字符串是否为python的标识符
# v1 = "abs23"
# v2 = "123abc"
# v3 = "_test_func"
# v4 = 'def'
# print(v1.isidentifier())
# print(v2.isidentifier())
# print(v3.isidentifier())
# print(v4.isidentifier())

'''
islower()   判断字符串是否都是小写
lower()  变小写

'''
# v1 = "adse_!@3"
# v2 = "abcdefAA"
# print(v1.islower())
# print(v2.islower())

# isnumeric() 判断字符串是否为  数字串
# v1 = "0123123"
# print(v1.isnumeric())


# isspace()  判断是否全是空格
# v1 = "      "
# v2 = "123   abc"
# print(v1.isspace())
# print(v2.isspace())

'''
title() 转换成标题格式字符串
istitle()  判断是否为标题格式的字符串

'''
# v1 = "This is a good"
# v2 = "This Is A Good Things"
# v3 = v1.title()
# print(v1.istitle())
# print(v2.istitle())
#
# print(v3)

'''
isupper() 判断是否全是大写
upper() 转为大写
'''

# v1 = "TTTTT"
# v2 = 'abcdefgAA'
# v3 = v2.upper()
# print(v1, v1.isupper())
# print(v2, v2.isupper())
# print(v3, v3.isupper())

'''
join()
字符串拼接插入
'''


# v1 = '-'.join("abc")
# print(v1)
# v2 = '*'.join(["mike","45","IT科技"])
# print(v2)

'''
ljust 长度为width的左对齐字符串。  
rjust  长度为width的右对齐字符串。 
'''

# v1 = "hello World"
# print(v1.ljust(40, '*'))
# print(v1.rjust(40, '*'))

'''
字符串分割
partition
rpartition
split
rsplit

'''
#
# v1 = "姓名.年龄.工作.工资.家庭"
# print(v1.rpartition("."))
# print(v1.rsplit("."))
# print(v1.partition("."))
# print(v1.split('.'))

# 去除字符串中的换行符
# v3 = "  1\n123123\n"
# print(v3.splitlines(False))
# print(v3.splitlines(True))


'''
lstrip   去除字符串左边的空格（或指定字符串）
rstrip    去除字符串右边的空格（或指定字符串）
strip    去除字符串两边的空格（或指定字符串）
'''

# v2 = "---123---"
# print(v2.rstrip('-'))
# print(v2.lstrip('-'))
# print(v2.strip('-'))



'''
swapcase()
字符串大小写转换，大写表小写，小写变大写
'''
# v1 = "abcDEF"
# print(v1.swapcase())

'''
字符串的切片操作
str1[start:end:step]

'''

str1 = ["zhang",1,3,54,34,23,1,2,3,4,5,6,7,8]

print(str1[2])
print(str1[-4])
print(str1[1:4])
print(str1[-4:-1])

print(str1[1:10:2])




'''
translate
zill

'''





