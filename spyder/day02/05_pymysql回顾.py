# coding=utf-8
import pymysql
import warnings

warnings.filterwarnings("ignore") #这是忽略警告的用法
#数据库连接对象
db=pymysql.connect(host="localhost",port=3306,user="root",passwd="123456",db="spider",charset='utf8')

#游标对象
cursor=db.cursor()

ins="insert into film(name,star,time) values (%s,%s,%s)"
#执行插入语句
ins=cursor.execute(ins,["霸王别姬","张国荣","1993"])
#提交
db.commit()
#关闭
cursor.close()
db.close()