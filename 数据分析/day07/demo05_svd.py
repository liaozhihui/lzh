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
vals[50:]=0
img2 = np.mat(vecs)*np.diag(vals)*np.mat(vecs).I
img2=img2.real

#奇异值分解
U,sv,V=np.linalg.svd(img)
sv[50:]=0
img3 = np.mat(U)*np.diag(sv)*np.mat(V)
img3=img3.real

mp.figure("EIG",facecolor='lightgray')
mp.subplot(221)
mp.xticks([])
mp.yticks([])
mp.imshow(img,cmap='gray')
mp.subplot(222)
mp.xticks([])
mp.yticks([])
mp.imshow(img2,cmap='gray')
mp.subplot(224)
mp.xticks([])
mp.yticks([])
mp.imshow(img3,cmap='gray')
mp.tight_layout()
mp.show()


