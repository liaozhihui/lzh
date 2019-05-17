# coding=utf-8
"""
傅里叶变换拆方波
"""
import numpy as np
import numpy.fft as nf
import matplotlib.pyplot as mp


x= np.linspace(-2*np.pi,2*np.pi,1000)
y = np.zeros(1000)
n = 1000

for i in range(1,n+1):
    y+=4/((2*i-1)*np.pi)*np.sin((2*i-1)*x)
mp.subplot(121)
mp.plot(x,y)

#针对y 做fft
y_complex = nf.fft(y)
print(y_complex,y_complex.dtype,y_complex.shape)
#逆向傅里叶变换
y2 = nf.ifft(y_complex).real
mp.plot(x,y2,label='y2',c='orangered',linewidth=7,alpha=0.4)

#绘制频域图像 频率/能量
freqs=nf.fftfreq(n,x[1]-x[0])
powers = np.abs(y_complex)
mp.legend()
mp.subplot(122)
mp.plot(freqs[freqs>=0],powers[freqs>=0],c='orangered',label='Freq Domin')
mp.legend()
mp.show()