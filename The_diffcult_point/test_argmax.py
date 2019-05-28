# coding=utf-8
import tensorflow as tf

a=tf.constant([[1,2,3],[2,3,4]])
b=tf.argmax(a,axis=0)
print(b)
