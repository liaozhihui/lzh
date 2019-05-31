# coding=utf-8
import tensorflow as tf
import numpy as np
import math
import collections
import pickle as pkl
import re
import jieba
import os.path as path

if __name__ == '__main__':
    stop_word=[]
    with open('stop_words.txt',encoding="utf-8") as f:
        line = f.readline()
        while line:
            stop_word.append(line[:-1])
            line=f.readline()
    stop_words=set(stop_word)
    print(stop_words)
    pass
