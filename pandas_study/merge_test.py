# coding=utf-8
import pandas as pd
import numpy as np

# left=pd.DataFrame({'key':['K0','K1','K2','K3'],
#                    'A':['A0','A1','A2','A3'],
#                    'B':['B0','B1','B2','B3']
#                    })
#
# right=pd.DataFrame({'key':['K0','K1','K2','K3'],
#                    'C':['C0','C1','C2','C3'],
#                    'D':['D0','D1','D2','D3']
#                    })
#
# print(left)
# print(right)
#
# res=pd.merge(left,right,on='key')
# print(res)
# left=pd.DataFrame({'key1':['K0','K0','K1','K2'],
#                     'key2':['K0','K1','K0','K1'],
#                    'A':['A0','A1','A2','A3'],
#                    'B':['B0','B1','B2','B3']
#                    })
#
# right=pd.DataFrame({'key1':['K0','K1','K1','K2'],
#                     'key2':['K0','K0','K0','K0'],
#                    'C':['C0','C1','C2','C3'],
#                    'D':['D0','D1','D2','D3']
#                    })
#
# #how:[left,right,inner,outer]
# # 默认的合并的方法方法是inner,找相同的
# #outer：都把key写出来的没有的表填nan
# #right:把右边的key为key,左边没有的用nan填充
# #left:同right
# res = pd.merge(left,right,on=['key1','key2'],how='right')
# print(res)

# df1=pd.DataFrame({'col1':[0,1],'col_left':['a','b']})
# df2=pd.DataFrame({'col1':[1,2,2],'col_right':[2,2,2]})
# print(df1)
# print(df2)
#
# #indicator参数
# #显示每行的合并情况PA
# #可以直接给indicator赋值,这是主要这列命名
# res = pd.merge(df1,df2,on='col1',how='outer',indicator=True)
# print(res)

# left=pd.DataFrame({'A':['A0','A1',"A2"],
#                    "B":['B0','B1',"B2"]},index=["K0","K1","K2"])
# right=pd.DataFrame({'C':['C0','C1',"C2"],
#                    "D":['D0','D1',"D2"]},index=["K0","K2","K3"])
# #left_index,right_index表示使用数据表的index
# res=pd.merge(left,right,left_index=True,right_index=True,how='outer')
# print(res)
boys=pd.DataFrame({'k':['K0','K1','K2'],'age':[1,2,3]})
girls=pd.DataFrame({'k':['K0','K0','K3'],'age':[4,5,6]})

res=pd.merge(boys,girls,on='k',suffixes=['_boys','_girls'],how="outer")
print(res)
