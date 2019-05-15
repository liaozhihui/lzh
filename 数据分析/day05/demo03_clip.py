# coding=utf-8
import numpy as np

a = np.arange(1,11)
print(a)
print(a.clip(min=5,max=8))
print(np.clip(a,5,8))
#np.any表示或
#np.all表示与
print(a.compress(np.all([a>3,a<8],axis=0)))