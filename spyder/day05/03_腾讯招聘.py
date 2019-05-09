# coding=utf-8
import requests
import json

headers={"User-Agent":"Mozilla/5.0"}
def get_page(url):
    res=requests.get(url,headers=headers)
    res.encoding = "utf-8"
    return json.loads(res.text)

def parse_page(html):
    for h in html['Data']["Posts"]:
        zh_name=h['RecruitPostName']
        zh_type=h["LocationName"]
        #一级页面获取PostId,详情页需要
        post_id = h['PostId']
        #通过F12抓包,抓到的地址如下
        two_url='https://careers.tencent.com/tencentcareer/api/post/ByPostId?timestamp=1557124084330&postId=%s&language=zh-cn'%post_id
        two_html = get_page(two_url)
        #职责
        duty=two_html['Data']['Responsibility']
        #要求
        require =two_html['Data']['Requirement']
        print(duty,require)
    pass
for index in range(1,11):
    url ="https://careers.tencent.com/tencentcareer/api/post/Query?timestamp=1557114145129&countryId=&cityId=&bgIds=&productId=&categoryId=&parentCategoryId=&attrId=&keyword=&pageIndex=%s&pageSize=10&language=zh-cn&area=cn"%(str(index))
    html = get_page(url)
    parse_page(html)
