# coding=utf-8
"""
图向量化
"""
import numpy as np
import matplotlib.pyplot as mp
import scipy.misc as sm
import  scipy.ndimage as sn
import sklearn.cluster as sc

img=sm.imread("../ml_data/lily.jpg",True)
x=img.reshape(-1,1)
model=sc.KMeans(n_clusters=6)
model.fit(x)
#返回类别标签
y=model.labels_
print(y,y.shape)

centers=model.cluster_centers_.ravel()
print(centers)
#使用掩码完成量化操作
img2=centers[y].reshape(img.shape)
mp.figure("Image Quant",facecolor="lightgray")
mp.subplot(121)
mp.xticks([])
mp.yticks([])
mp.imshow(img,cmap="gray")
mp.subplot(122)
mp.xticks([])
mp.yticks([])
mp.imshow(img2,cmap="gray")
mp.tight_layout()
mp.show()