import pandas as pd
import numpy as np
# 创建一组Series数据
# 1.创建Series
# s1=pd.Series(data=[90,86,70],index=["leo",'kate','john'])
# print(s1)
# #通过绝对位置
# print(s1[0])
# #通过标签
# print(s1['leo'])
# #通过列表
# print(s1[['leo','kate']])
# #通过表达式
# print(s1[s1>80])
# # 2.numpy中的ndarray：
# s2=pd.Series(data=np.random.randn(5),index=list('ABCDE'))
# # print(s2)
# # 3.数字创建
# s3=pd.Series(6)
# # 4.创建一组DataFrame数据-date_range创建时间
date=pd.date_range(start='20100101',periods=6,dtype='int32')
df=pd.DataFrame(data=np.random.randn(6,4),index=date,columns=list('abcd'))
# print(df)
# #数据形状
# print(df.shape)
# #数据元素
# print(df.values)
# #单列数据额访问
# print(df.a)
# print(df['a'])
# #多列数据的访问
# print(df[['a','b']])
# print(df.head(2))
# print(df[0:2])
# 使用loc
print(df.loc['2010-01-01':"2010-01-04",['a','b']])
#使用iloc查找
print(df.iloc[:4,[0,1]])
#使用ix查找
print(df.ix[:4,['a','b']])
#得到１月4号之前的
print(df.loc[df.index<'20100104'])
