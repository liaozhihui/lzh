# coding=utf-8
import numpy as np
import scipy.integrate as si
import matplotlib.pyplot as mp

def f(x):
    return 2*x**2+3*x+4
x=np.linspace(-5,5,100)
print(x)

val=si.quad(f,-5,5)
print(val)  #val[0]:积分值 val[1]:积分误差

f_vec=np.vectorize(f)
y=f_vec(x)
print(y)
mp.plot(x,y,c="orangered",label="integrate")
mp.legend()
mp.show()