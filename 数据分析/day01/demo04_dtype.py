# coding=utf-8
import numpy as np

data=[('zs',[90,80,70],15),('ls',[99,89,79],16),('ww',[91,81,71],17)]
ary = np.array(data,dtype="U2,3int32,int32")
print(ary,ary.dtype)

#第二种设置dtype的方式,为每个字段 ,为每个字段起别名

ary = np.array(data,dtype=[("name","str_",2),("scores","int32",3),('age','int32',1)])
print(ary[2]['age'])

#第三种设置dtype的方式
ary = np.array(data,dtype={"names":["name",'scores','age'],
                           "formats":['U2','3int32','int32']})
#第四种设置dtype的方式 手动指定每个字段的存储偏移字节书
#name 从0字节开始输出，输出3个unicode
#score 从16字节开始输出，输出3个int32
ary = np.array(data,dtype={"name":('U3',0),'scores':('3int32',16),"age":('int32',28)})

#ndarray数组中存储日期类型数据

dates = np.array(['2011','2012-01-01','2013-01-01 11:11:11','2011-02-01'])
print(dates,dates.dtype)
dates = dates.astype('M8[D]') #datetime64 精确到Day
print(dates,dates.dtype)