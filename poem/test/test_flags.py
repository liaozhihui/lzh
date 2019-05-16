# coding=utf-8
import tensorflow as tf
tf.app.flags.DEFINE_integer('batch_size',64,"batch size.")
tf.app.flags.DEFINE_float("learning_rate",0.01,'learning rate.')


fla=tf.app.flags.FLAGS
print(fla.learning_rate)
print(fla.batch_size)