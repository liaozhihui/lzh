# coding=utf-8
import pymongo

db_name="maoyandb"
set_name="film"

#1、连接对象
conn = pymongo.MongoClient('localhost',27017)
#2、库对象
db=conn[db_name]
#3、集合对象
myset=db[set_name]

#执行插入语句
myset.insert_one({'name':"TieChui"})