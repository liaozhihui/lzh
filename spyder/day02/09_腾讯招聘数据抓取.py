# coding=utf-8
import requests
from urllib import parse
import re
import time
import pymongo
import pymysql
import warnings
warnings.filterwarnings('ignore')
class TencentSpidder(object):

    def __init__(self):
        self.headers={"User-Agent":"Mozila/5.0"}
        self.baseurl="https://hr.tencent.com/position.php?start="
        # self.conn=pymongo.MongoClient('localhost',27017)
        # self.db=self.conn['Tencent']
        # self.myset=self.db['jobs']
        self.db=pymysql.connect(host="localhost",port=3306,user='root',passwd='123456',charset='utf8')
        self.cursor=self.db.cursor()


    def get_job_info(self,url):
        #发请求获取响应内容html

        #用正则提取html中数据

        res=requests.get(url,headers=self.headers)
        res.encoding='utf-8'
        html=res.text

        #用正则提取html中数据
        p = re.compile('<td class="l square">.*?href="(.*?)">(.*?)</a>.*?<td>(.*?)</td>.*?<td>(.*?)</td>.*?<td>(.*?)</td>.*?<td>(.*?)</td>',re.S)
        job_info_list = p.findall(html)
        self.write_data(job_info_list)
    def get_job_duty(self,url):
        res=requests.get(url,headers=self.headers)
        res.encoding='utf-8'
        html = res.text

        p=re.compile('<ul class="squareli">(.*?)</ul>',re.S)
        duty_requie_list = p.findall(html)
        duty = duty_requie_list[0].strip().replace("<li>","").replace("</li>","")
        require = duty_requie_list[1].strip().replace("<li>","").replace("</li>","")
        return duty,require
    def write_data(self,job_info_list):
        sql1="create database if not exists Tencent"
        self.cursor.execute(sql1)
        self.cursor.execute("use Tencent")
        sql2="""create table if not exists jobs 
(id int primary key auto_increment,
name varchar(50),type varchar(50),
num int,address varchar(50),
time varchar(50),
dutys text,
requires text) charset=utf8;"""

        self.cursor.execute(sql2)
        ins="insert into jobs(name,type,num,address,time,dutys,requires) values(%s,%s,%s,%s,%s,%s,%s)"
        for job in job_info_list:
            #job_duty job_requirement
            job_url='https://hr.tencent.com/'+job[0].strip()
            job_duty,job_requirement=self.get_job_duty(job_url)
            # job_dict={
            #     "职位连接":job[0].strip(),
            #     "职位名称":job[1].strip(),
            #     "职位类别":job[2].strip(),
            #     "招聘人数":job[3].strip(),
            #     "地址":job[4].strip(),
            #     "时间":job[5].strip(),
            #     "工作职责":job_duty,
            #     "工作要求":job_requirement
            #           }
            job_list = [job[1].strip(),job[2].strip(),job[3].strip(),job[4].strip(),job[5].strip(),job_duty,job_requirement]
            print(job_list)

            self.cursor.execute(ins,job_list)
    def main(self):
        job_type = input("Input Job Type:")

        for pn in range(0,301,10):
            params = {'keywords':job_type,'start':str(pn)}
            params =parse.urlencode(params)
            url = self.baseurl + params
            self.get_job_info(url)
        # url="https://hr.tencent.com/position.php?start=0"
        # self.get_job_info(url)
        self.cursor.close()
        self.db.close()

if __name__=="__main__":
    start=time.time()
    spider=TencentSpidder()
    spider=spider.main()
    end=time.time()
    print(end-start)
