# -*- encoding=utf8 -*- 
'''
@Time:  2022/4/19-13:58
@User:  Administrator
@File:  函数练习1.py
@Email：  liuxiong@fcbox.com
'''

def check_str(msg):
    res = {
        "num":0,
        "string":0,
        "space":0,
        "other":0
    }

    for s in msg:
        if s.isdigit():
            res['num'] +=1
        elif s.isalpha():
            res["string"] +=1
        elif s.isspace():
            res["space"] +=1
        else:
            res["other"] +=1

    return res


# strs = "ab3 c123 .34 65 hgdh?!@3"
# res = check_str(strs)
# print(res)

def check_length(ss):
    '''

    :param list: 列表 元组 字符串
    :return:
    '''
    l = len(ss)
    if l>5:
        print("输入的类型为：%s 长度%s"%(type(ss),l))
    else:
        print("长度小于等于5")
#
# check_length("123123")


def check_list(lists):
    '''
    检查列表的长度
    :param lists:
    :return:
    '''
    l = len(lists)
    if l>2:
        return lists[:2]
    else:
        return lists

# res = check_list([1])
# print(res)

def check_list_or_tuple(ss):
    '''
    获取列表 元组的奇数位
    :param ss:
    :return:
    '''
    return ss[::2]

res = check_list_or_tuple([1,2,3,4,5,6,7,8,9,10])
print(res)