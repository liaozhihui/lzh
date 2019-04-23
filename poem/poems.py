# coding=utf-8
import collections
import os
import sys
import numpy as np

start_token = "G"
end_token="E"

def process_poems(file_name):
    #诗集
    poems=[]
    with open(file_name,'r',encoding='utf-8') as f:
        for line in f.readlines():
            try:
                title,content=line.strip().split(':')
                content = content.replace(' ','')
                if '_' in content or "(" in content or "{" in content or "{" in content \
                    or "<<" in content or "[" in content or start_token in content or\
                    end_token in content:
                    continue
                if len(content) <5 or len(content) >79:
                    continue
                content=start_token+content+end_token
                poems.append(content)
            except ValueError as e:

                pass
    #按诗的字数排序
    print(poems)
    poems = sorted(poems,key = lambda line:len(line))
    print(poems)
process_poems("./data/poetry.txt")
