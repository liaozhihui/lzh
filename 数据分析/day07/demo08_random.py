# coding=utf-8
import numpy as np

#篮球案例   命中率0.8

a = np.random.binomial(10,0.8,100000)
print(len(a[a==5]))

#超集合分布
b=np.random.hypergeometric(6,4,3,100000)
print((b==0).sum()/100000)

#正态分布
print(np.random.normal(0,1,10))
#平均分布
print(np.random.uniform(1,10,10))