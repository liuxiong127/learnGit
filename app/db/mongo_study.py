# -*- encoding=utf8 -*- 
'''
@Time:  2021/4/19-11:14
@User:  Administrator
@File:  mongo_study.py
@Email：  liuxiong@fcbox.com
'''

import pymongo

myclient = pymongo.MongoClient('mongodb://localhost:27017/')


# 查询数据库名称
dblist = myclient.list_database_names()
# print(dblist)
mydb = myclient["runoobdb"]
mycol = mydb['sites']

mydict = {"name":"runoob", "address":"湖北省武汉市", "url":"http://www.baidu.com/"}
# mydict1 = {"_id":"123456789","name":"runoob", "address":"湖北省武汉市", "url":"http://www.baidu.com/"}
x = mycol.insert_one(mydict)
# # y = mycol.insert_one(mydict1)
# print(x)
# # print(y)
# print(x.acknowledged, x.inserted_id)
#
# mylist = [
#   { "name": "Taobao", "alexa": "100", "url": "https://www.taobao.com" },
#   { "name": "QQ", "alexa": "101", "url": "https://www.qq.com" },
#   { "name": "Facebook", "alexa": "10", "url": "https://www.facebook.com" },
#   { "name": "知乎", "alexa": "103", "url": "https://www.zhihu.com" },
#   { "name": "Github", "alexa": "109", "url": "https://www.github.com" }
# ]
#
# z = mycol.insert_many(mylist)
# print(z.inserted_ids)


# res = mycol.find_one()
# res1 = mycol.find()
# res2 = mycol.find({'name':"runoob"})
# print(res2)
# print(res)
#
#
# for i in res1:
# #     print(i)
#
# print("1111111111111111111")
#
# for i in res2:
#     print(i)


# res = mycol.find_one()
# query = {"name": {"$regex":"^r"}}
# res1 = mycol.find_one(query)
# res2 = mycol.find(query).limit(1)
# print(res1)
# print(res2)
#
# for i in res2:
#     print(i)

# 更新值
# query = {"name":"runoob"}
# newvalues = {"$set":{"name":"test1234"}}
# mycol.update_one(query, newvalues)
# for x in mycol.find():
#     print(x)

# 排序
# mydoc = mycol.find().sort("name")
# for x in mydoc:
#     print(x)
#


# # 删除
# query1 = {"name":"test1234"}
# res = mycol.delete_one(query1)
# print(res)
# print(res.deleted_count)
#
# for x in mycol.find():
#     print(x)

for i in mycol.find():
    print(i)

# x1 = mycol.delete_many({})
x1 = mycol.delete_many({"_id":{"$exists":True}})
print(x1.deleted_count, "删除数量")


