# coding=utf-8
import numpy as np
import os
import string

cn_punctuation_set = ['，', '。', '！', '？', '"', '"', '、']
en_punctuation_set = [',', '.', '?', '!', '"', '"']

def clean_cn_corpus(file_name,clean_level='all',simple_only=True,is_save=True):
    if os.path.dirname(file_name):
        base_dir=os.path.dirname(file_name)
    else:
        print("没有该文件")
    save_file=os.path.join(base_dir)

    with open(file_name,"r+",encoding='utf-8') as f:
        clean_countent=[]