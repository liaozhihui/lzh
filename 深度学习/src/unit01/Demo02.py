# coding=utf-8
import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np

x=np.array([[1,0],[0,0],[0,1],[1,1],[1,1],[1,1]])

y=np.array([[0],[0],[0],[1],[1],[1]])
def plot_data(x,y):
    y=y.flatten()
    colors=["red" if y_>0 else "green" for y_ in y   ]
    plt.figure()
    # print(colors)

    plt.scatter(x[:,0],x[:,1],c=colors,label="And",s=90)
    plt.show()

# plot_data(input_x,y)
def plot_data1(x,y):
    y1=y.flatten() #对y进行维度调整,由2维变为１维的
    index0=np.where(y1==0)
    index1=np.where(y1==1)
    plt.figure()
    plt.scatter(x[index0,0],x[index0,1],c='r',marker='o',s=20)
    plt.scatter(x[index1,0],x[index1,1],c='g',marker='o',s=20)
    plt.show()
# plot_data1(input_x,y)

#构建模型，
#超参数：超参数 模型的层数，每层神经元的数量，神经元之间的连接方式

input_x=tf.placeholder(dtype=tf.float32,shape=[None,2])
output_y=tf.placeholder(dtype=tf.float32,shape=[None,1])

weights=tf.Variable(tf.random_normal(shape=[2,1],stddev=0.01))

bias=tf.Variable(tf.random_normal(shape=[1],stddev=0.01))

hy=tf.sigmoid(tf.matmul(input_x,weights)+bias)

# 损失函数
loss =-tf.reduce_mean(output_y*tf.log(hy)+(1-output_y)*tf.log(1-hy))

# 优化
op = tf.train.GradientDescentOptimizer(learning_rate=0.1).minimize(loss)

#性能评估,预测准确率
output=tf.cast(hy>0.5,tf.float32)
cur=tf.reduce_mean(tf.cast(tf.equal(output,output_y),tf.float32))

# m1=tf.constant([[1,2,3],[4,5,6]])
# m2=tf.constant([[1,1,1],[1,1,1]])
# m3=m1+m2
# print(type(m3))
# print(m3)


# m4=tf.Variable(tf.random_normal(shape=[2,3],stddev=0.01))
#
# #占位符
# m5=tf.placeholder(dtype=tf.float32,shape=[1],name='m5')
# m6=tf.placeholder(dtype=tf.float32,shape=[1],name='m6')
# m7=m5+m6

session = tf.Session()
with tf.Session() as session:
    session.run(tf.global_variables_initializer())
    for i in range(2001):
        l,o,c=session.run([loss,op,cur],feed_dict={input_x:x,output_y:y})
        print("第{0}次迭代,损失值:{1},正确率:{2}".format(i+1,l,c))


    # result=session.run(m4)
    # print(result)
    # result2=session.run(m7,feed_dict={m5:[1],m6:[2]})
    # print(result2)

    predict = session.run(output,feed_dict={input_x:[[0,0],[0,1],[1,1]]})
    print(predict)

