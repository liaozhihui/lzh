# coding=utf-8
import pandas as pd
import jieba

df_news=pd.read_table('./data/val.txt',names=['category','theme',"URL",'content'],encoding="utf-8")
df_news=df_news.dropna()
print(df_news.shape)

content=df_news.content.values.tolist()
print(content[1000])

content_S=[]
for line in content:
    current_segment = jieba.lcut(line)
    if len(current_segment) >1 and current_segment !="\r\n":
        content_S.append(current_segment)