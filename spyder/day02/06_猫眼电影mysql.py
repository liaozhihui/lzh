# coding=utf-8
from urllib import request,parse
import re
import pymongo
import pymysql
import re
class CatEyeSpider(object):

    def __init__(self,baseurl,user_agent):
        self.baseurl=baseurl
        self.user_agent=user_agent
        self.db=pymysql.connect(host="localhost",port=3306,user="root",passwd="123456",db="spider",charset='utf8')
        self.cursor=self.db.cursor()


    def get_page(self,key):
        key=parse.urlencode(key)
        url=self.baseurl+key
        req=request.Request(url,headers=self.user_agent)
        res=request.urlopen(req)
        html=res.read().decode("utf-8")
        return html

    def parse_page(self,html):
        content="""<p class="name"><a href="/films/592" title="狮子王" data-act="boarditem-click" data-val="{movieId:592}">狮子王</a></p>
            <p class="star">
            主演：马修·布罗德里克,尼基塔·卡兰姆,詹姆斯·厄尔·琼斯
            </p>
            <p class="releasetime">上映时间：1995-07-15</p>    </div>"""

        p=re.compile('<p class="name">.*?title="(.*?)".*?<p class="star">(.*?)</p>.*?<p class="releasetime">(.*?)</p>.*?</div>',re.S)
        p_list=p.findall(html)
        return p_list
    #保存到mongo
    def write_page(self,p_list):
        ins="insert into film(name,star,time) values(%s,%s,%s)"
        for rt in p_list:
            film_list=[rt[0].strip(),rt[1].strip(),re.findall("\d{4}-?\d{0,2}-?\d{0,2}",rt[2].strip())[0]]
            self.cursor.execute(ins,film_list)
        self.db.commit()







    def main(self):
        p_list=[]
        for i in range(5):
            key={"offset":i*10}
            html=self.get_page(key)
            result=self.parse_page(html)
            p_list+=result
        self.write_page(p_list)
        self.cursor.close()
        self.db.close()



if __name__=="__main__":
    baseurl="https://maoyan.com/board/4?"
    user_agent={"User-Agent":"Opera/8.0 (Windows NT 5.1; U; en)"}
    spider=CatEyeSpider(baseurl,user_agent)
    spider.main()