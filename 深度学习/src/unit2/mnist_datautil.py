# coding=utf-8
from tensorflow.examples.tutorials.mnist import input_data
import numpy as np
import matplotlib.pyplot as plt


#加载数据

#加载数据
def load_data(filename):
    mnist=input_data.read_data_sets('../../dataset/mnist',one_hot=True)
    mnist.train.cls=np.argmax(mnist.train.labels,axis=1)
    mnist.validation.cls=np.argmax(mnist.validation.labels,axis=1)
    mnist.test.cls=np.argmax(mnist.test.labels,axis=1)
    return mnist

#测试
mnist=load_data('../../dataset/mnist')


#数据可视化

def plt_data(imgs,cls,pred=None):
    assert len(imgs)==len(cls)==9
    fig,axs=plt.subplots(3,3)
    for i ,ax in enumerate(axs.flat):
        ax.imshow(imgs[i].reshape(28,28),cmap="binary")
        lbl=" " #文字
        if pred is None:
            lbl='cls:{0}'.format(cls[i])
        else:
            lbl='cls:{0};pred{1}'.format(cls[i],pred[i])
        ax.set_xlabel(lbl)
        ax.set_xticks([])
        ax.set_yticks([])
    plt.show()

# plt_data(mnist.train.images[:9],mnist.train.cls[:9])
