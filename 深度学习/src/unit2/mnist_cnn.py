# coding=utf-8
import tensorflow as tf
import numpy as np
from mnist_datautil import *

#构建模型
#--输入层
input_x = tf.placeholder(shape=[None,784],dtype=tf.float32)
input_img=tf.reshape(input_x,shape=[-1,28,28,1]) #符合cnn结构的要求的矩阵形状
#--输出层
output_y=tf.placeholder(shape=[None,10],dtype=tf.float32)
output_cls=tf.argmax(output_y,dimension=1)
#--conv1 : 输出[-1,28,28,32]
conv1=tf.layers.conv2d(inputs=input_img,filters=32,kernel_size=[5,5],padding='same',activation=tf.nn.relu)
#--pool1 :输出[-1,14,14,32]
pool1=tf.layers.max_pooling2d(conv1,pool_size=(2,2),strides=(2,2))
#--conv2 :输出[-1,14,14,64]
conv2=tf.layers.conv2d(inputs=pool1,filters=64,kernel_size=[5,5],padding='same',activation=tf.nn.relu)
#--pool2 :输出[-1,7,7,64]
pool2=tf.layers.max_pooling2d(conv2,pool_size=(2,2),strides=(2,2))

#--全连接层

flat=tf.reshape(pool2,shape=[-1,7*7*64])
#降采样
dp=tf.layers.dropout(inputs=flat,rate=0.4)
fc=tf.layers.dense(inputs=dp,units=1024,activation=tf.nn.relu)

output=tf.layers.dense(inputs=fc,units=10)
output=tf.nn.softmax(output)

#定义损失函数,计算误差值
loss=tf.nn.softmax_cross_entropy_with_logits(labels=output_y,logits=output)
loss=tf.reduce_mean(loss) #均值误差
#定义优化器进行调参
op=tf.train.AdamOptimizer(learning_rate=1e-4).minimize(loss)

#性能评估
output_pred=tf.argmax(output,dimension=1) #预测的数字
cur=tf.reduce_mean(tf.cast(tf.equal(output_pred,output_cls),tf.float32))


#定义批次大小
batch_size=64
#最优准确率
best_cur=0
#模型存储
saver=tf.train.Saver()


with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    checkpoint = tf.train.latest_checkpoint("checkpoint")
    print(checkpoint)
    if checkpoint:
        saver.restore(sess, checkpoint)
        pred=sess.run(output_pred,feed_dict={input_x:mnist.test.images[:9]})
        print(pred)
        print(mnist.test.cls[:9])
        # plt_data(mnist.test.images[:9],mnist.test.cls[:9],pred)
    else:

        for i in range(1001):
            train_x,train_y=mnist.train.next_batch(batch_size)
            c,_=sess.run([cur,op],feed_dict={input_x:train_x,output_y:train_y})
            if(c>best_cur):
                best_cur=c
                saver.save(sess,save_path="checkpoint/best",global_step=i)
            if(i%200==0):
                print("iter:{0},cur{1}".format(i+1,c))












