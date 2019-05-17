# coding=utf-8
'''
提取图片特征值
'''
import numpy as np
import scipy.misc as sm
import matplotlib.pyplot as mp
#True:提取图片亮度矩阵   二维
#False:提取图片颜色矩阵  三维
img=sm.imread('../da_data/lily.jpg',True)
print(type(img),img.shape,img.dtype)
print(img[0,0])
vals,vecs = np.linalg.eig(img)
vals[1:]=0
img2 = np.mat(vecs)*np.diag(vals)*np.mat(vecs).I
img2=img2.real

mp.figure("EIG",facecolor='lightgray')
mp.subplot(121)
mp.xticks([])
mp.yticks([])
mp.imshow(img,cmap='gray')
mp.subplot(122)
mp.xticks([])
mp.yticks([])
mp.imshow(img2,cmap='gray')
mp.tight_layout()
mp.show()


