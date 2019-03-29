import tensorflow as tf
import numpy as np
import pickle
class word2vec(object):
    def __init__(self,
                 vocab_list=None,
                 embeding_size=20,
                 win_len=3,
                 learning_rate = 0.01,
                 num_sample = 100,model_path=None):
        self.batch_size=None
        if model_path !=None:
            self.load_model(model_path)
        else:
            assert type(vocab_list) == list
            self.vocab_list=vocab_list
            self.vocab_size=vocab_list.__len__()
            self.win_len=win_len
            self.num_sample=num_sample
            self.learning_rate=learning_rate
            self.word2id={}
            for i in range(self.vocab_size):
                self.word2id[self.vocab_list[i]] = i

#创建模型，训练
f=open("word_list.pkl",'rb')
word_list=pickle.load(f)[0]["萧炎"]
f.close()
print(word_list)
w2v = word2vec(vocab_list=word_list,
                            embeding_size=200,
                            win_len=2,
                            learning_rate=0.01,
                            num_sample=100)    #负采样


