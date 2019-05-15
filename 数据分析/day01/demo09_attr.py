# coding=utf-8
import numpy as np

data = np.array([[1+1j,2+1j,3+1j],
                [4+1j,5+1j,6+1j],
                [7+3j,8+6j,9+9j]])
print(data.ndim)
print(data.dtype,data.itemsize)
print(data.nbytes)
print(data.real)
print(data.imag)
print(data.T)
print([x for x in data.flat])
