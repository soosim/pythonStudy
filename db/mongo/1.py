# coding:utf-8
from pymongo import MongoClient

client = MongoClient("127.0.0.1",27017)
db = client.xie
collect = db.xie
data = {
    "title":"test mongo",
    "content":"phjsahfjhjg"
}
result = collect.insert_one(data)
print(result)

for i in db.xie.huan.find():
    print(i)
