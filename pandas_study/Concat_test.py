# coding=utf-8
import numpy as np
import pandas as pd

# df1=pd.DataFrame(np.ones((3,4))*0,columns=['a','b','c','d'])
# df2=pd.DataFrame(np.ones((3,4))*1,columns=['a','b','c','d'])
# df3=pd.DataFrame(np.ones((3,4))*2,columns=['a','b','c','d'])
#
# result=pd.concat([df1,df2,df3],axis=0,ignore_index=True)
# print(result)

df1=pd.DataFrame(np.ones((3,4))*0,columns=['a','b','c','d'],index=[1,2,3])
df2=pd.DataFrame(np.ones((3,4))*1,columns=['b','c','d','e'],index=[2,3,4])
print(df1)
print(df2)
print("="*40)
res=pd.concat([df1,df2])
print(res)
#join:
#默认是outer模式,将两张表合并,没有的取nan
#如果是inner,则取两张表共有的
res2=pd.concat([df1,df2],join="inner",ignore_index=True)
print("="*40)
print(res2)

#join_axes：
#表示以哪张表的行或为主
res3=pd.concat([df1,df2],join_axes=[df1.columns])
print("="*40)
print(res3)
