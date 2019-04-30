# coding=utf-8
from urllib import request,parse

class BaiduSpider(object):
    def __init__(self):
        self.baseurl="http://tieba.baidu.com/f?"
        self.headers={"User-Agent":"Opera/8.0 (Windows NT 5.1; U; en)"}
        print(self.baseurl)
    #获取页面
    def get_page(self,url):
        req=request.Request(url,headers=self.headers)
        res=request.urlopen(req)
        html=res.read().decode("utf-8")
        return html
    #解析页面
    def parse_page(self):
        pass
    #保存页面
    def write_page(self,html,filename):
        with open(filename,"w") as f:
            f.write(html)

    #主函数
    def main(self):
        name = input("请输入贴吧名称:")
        begin = int(input("请输入起始页:"))
        end = int(input("请输入终止页:"))

        # 发请求保存数据
        for page in range(begin, end + 1):
            pn = (page - 1) * 50
            url = self.baseurl + parse.urlencode({"kw": name, "pn": str(pn)})
            html=self.get_page(url)
            filename="{}-第{}页.html".format(name,page)
            self.write_page(html,filename)


            print("第%s页爬取成功" % page)
if __name__=="__main__":
    spider=BaiduSpider()
    spider.main()