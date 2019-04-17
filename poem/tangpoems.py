# coding=utf-8
import collections
import os
import sys
import numpy as np
import tensorflow as tf
# from model import rnn_model
# from poems import process_poems,generate_batch
import heapq

tf.app.flags.DEFINE_integer('batch_szie',64,'batch size')
tf.app.flags.DEFINE_float("learning_rate",0.01,'learning rate')