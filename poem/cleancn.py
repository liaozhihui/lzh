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
    save_file=os.path.join(base_dir,os.path.basename(file_name).split('.')[0]+'cleaned.txt')

    with open(file_name,"r+",encoding='utf-8') as f:
        clean_content=[]
        for l in f.readlines():
            l=l.strip()
            if l=='':
                pass
            else:
                l=list(l)
                should_remove_words=[]

                for w in l:
                    if not should_reserve(w,clean_level):
                        should_remove_words.append(w)
                clean_line=[c for c in l if c not in should_remove_words]
                clean_line=''.join(clean_line)
                if clean_line !='':
                    clean_content.append(clean_line)
    if is_save:
        with open(save_file,'w+') as f:
            for l in clean_content:
                f.write(l+'\n')
        print("[INFO]cleaned file have been saved to %s"%save_file)
    return clean_content

def should_reserve(w,clearn_level):
    if w=='':
        return True
    else:
        if clearn_level=="all":
            if w in cn_punctuation_set or w in string.punctuation or is_alphabet(w):
                return False
            else:
                return is_chinese(w)

        elif clearn_level=="normal":
            if is_chinese(w) or is_alphabet(w) or is_number(w):
                return True
            elif w in cn_punctuation_set or w in en_punctuation_set:
                return True
            else:
                return False
        elif clearn_level=="clean":
            if is_chinese(w):
                return True
            elif w in cn_punctuation_set:
                return True
            else:
                return False
        else:
            raise "clean_level not support %s,please set for all,normal,clean"%clearn_level


def is_number(uchar):
    if u'\u0030' <= uchar <=u'\u0039':
        return True
    else:
        return False


def is_alphabet(uchar):
    if (u'\u0041' <= uchar <=u'\u005a') or (u'\u0061' <= uchar <=u'\u007a'):
        return True
    else:
        return False

def is_chinese(uchar):
    if u'\u4e00' <= uchar <=u'\u9fa5':
        return True
    else:
        return False

def semi_angle_to_sbc(uchar):
    '''半角转全角'''
    inside_code = ord(uchar)
    if inside_code <0x0020 or inside_code > 0x7e:
        return uchar

    if inside_code == 0x0020:
        inside_code = 0x3000
    else:
        inside_code += 0xfee0
    return chr(inside_code)

def sbc_to_semi_angle(uchar):
    '''全角转半角'''
    inside_code = ord(uchar)

    if inside_code == 0x3000:
        inside_code = 0x0020
    else:
        inside_code -=0xfee0
    if inside_code <0x0020 or inside_code > 0x7e:
        return uchar

    return chr(inside_code)
