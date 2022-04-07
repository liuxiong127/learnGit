# -*- encoding=utf8 -*- 
'''
@Time:  2022/4/6-13:30
@User:  Administrator
@File:  python基础(字典).py
@Email：  liuxiong@fcbox.com
'''

'''
字典：
标识符：dict

'''

# d1 = {"name":"张仁杰", "age":45, "job":"IT"}
# 字典的取值
# print(d1["name"])
# print(d1.get("age"))



# 字典清空
# d1.clear()
# print(d1)

# # 字典的遍历
# for i in d1:
#     print(i)

# 字典的键

# for i in d1.keys():
#     print(i)
# 字典的值
# for i in d1.values():
#     print(i)
# 字典的键和值
# for i in d1.items():
#     print(i, type(i))


# 判断键是否存在
# if "name" in d1.keys():
#     print("name存在")
# else:
#     print("name不存在！！")


# 字典的长度
# print(len(d1))
# 通过使用新的索引键并为其赋值，可以将项目添加到字典中
# d1["color"] = "red"
# print(d1)
# print("--------------")
# 删除项目或索引键
# d1.pop("color")
# print(d1)
# d1.popitem()
# print(d1)
# del d1["age"]
# print(d1)
# d1.clear()# 清空字典
# print(d1)


# 复制字典
# d2 = d1.copy()
# d1["name"] = "鲁智深"
# print(d1)
# print(d2)

# 字典更新
# d1.update({"name":"guoqing"})
#
# print(d1)

'''
字典的键必须要是可hash的数据类型，即 字符串，数值，布尔，元组
不能是：列表 ，字典，集合
'''

d1 = {
    "name":"jack",
    2:"主干道",
    True:3,
    (1,2,):"元组",
    {"test":"2"}:4

}
print(d1)
dict