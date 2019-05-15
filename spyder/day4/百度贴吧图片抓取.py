# coding=utf-8
import requests
from lxml import etree

class Baiduspider(object):
    def __init__(self):
        self.baseurl="http://tieba.baidu.com/f?"
        #使用IE的User-Agent
        self.headers={"User-Agent":'Mozilla/5.0'}
    #获取帖子连接
    def get_turl(self,params):
        res=requests.get(self.baseurl,params=params,headers=self.headers)

        res.encoding="utf-8"
        html = res.text

        #提取帖子链接：
        parse_html=etree.HTML(html)

        t_list = parse_html.xpath('//div[@class="t_con cleafix"]/div/div/div/a/@href')
        print(t_list)
        for t in t_list:
            url = "http://tieba.baidu.com"+t
            #提取图片链接，对图片链接发请求保存到本地
            self.get_imgurl(url)

    def get_imgurl(self,url):
        res = requests.get(url,headers=self.headers)
        res.encoding = 'utf-8'
        html = res.text
        parse_html = etree.HTML(html)
        img_list = parse_html.xpath('//div[@class="d_post_content_main d_post_content_firstfloor"]//img[@class="BDE_Image"]/@src')
        # img_list = parse_html.xpath('//video/@src')

        print(img_list)
        for img in img_list:
            self.write_Img(img)

    #保存图片
    def write_Img(self,img):
        res = requests.get(img,headers = self.headers)
        res.encoding = "utf-8"
        html = res.content
        filename=img[-10:]
        with open(filename,'wb') as f:
            f.write(html)
            print("%s下载成功"%filename)
    #主函数
    def main(self):
        name = input("贴吧名:")
        begin = int(input("起始页:"))
        end = int(input("终止页:"))
        for page in range(begin,end+1):
            pn = (page-1) * 50
            params = {
                'kw':name,
                'pn':str(pn)
            }
            self.get_turl(params=params)

if __name__ == '__main__':
    spider = Baiduspider()
    spider.main()