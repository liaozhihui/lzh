#coding:utf-8
from collections import Counter
import jieba
import pickle


def wordList():

    stop_words=[]
    stop_words_append=stop_words.append
    with open(u'stop_words.txt',encoding='utf-8') as f:
        line = f.readline()
        while line:
            stop_words_append(line[:-1])
            line=f.readline()
    stop_words.insert(0,u'\n')

    raw_word_list=[]
    raw_sentence=[]
    raw_sentence_append=raw_sentence.append
    with open(u'2800.txt',encoding='gbk') as f:
        line=f.readline()
        while line:
            if len(line)>1:
                temp=[i for i in jieba.cut(line) if i not in stop_words]
                raw_word_list+=temp
                raw_sentence_append(temp)
            line=f.readline()


    return raw_word_list,raw_sentence,stop_words

def word2Id_id2Word(word_list,vocab_size=None):

    id2Word={}
    a=Counter(word_list).most_common(vocab_size)

    for id,value in enumerate(a):
        id2Word[id] = value[0]
    f = open("word_list.pkl", 'wb')
    word2Id = dict(zip(id2Word.values(),id2Word.keys()))
    pickle.dump([word2Id, id2Word], f, True)
    f.close()
    return word2Id,id2Word


if __name__=="__main__":
    raw_word_list, raw_sentence,_=wordList()
    word2Id,id2Word = word2Id_id2Word(raw_word_list)






