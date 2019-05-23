import pandas as pd
import numpy as np
data = pd.DataFrame({'Sample': range(1, 11), 'Gender': ['Female', 'Male', 'Female', 'Male', 'Male', 'Male', 'Female', 'Female', 'Male', 'Female'],
                    'Handedness': ['Right-handed', 'Left-handed', 'Right-handed', 'Right-handed', 'Left-handed', 'Right-handed', 'Right-handed', 'Left-handed', 'Right-handed', 'Right-handed']})
print(data)
# 方法一：用pivot_table
r1=pd.pivot_table(data,index="Gender",columns="Handedness",values="Sample",margins=True,aggfunc=len)
r1=data.pivot_table(index="Gender",columns="Handedness",values="Sample",margins=True,aggfunc=len)
print(r1)
# 方法二：用crosstab
# crosstab()的前两个参数可以是数组、Series或数组列表
r2=pd.crosstab(index=data.Gender,columns=data.Handedness,values=data.Sample,margins=True,aggfunc=len)
print(r2)
