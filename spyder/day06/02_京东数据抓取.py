# coding=utf-8

import time
from selenium import webdriver

class JdSpider(object):
    def __init__(self):
        self.browser=webdriver.PhantomJS()
        self.url = "http://www.jd.com/"


    #获取商品页面
    def get_page(self):
        self.browser.get(self.url)
        #找两个节点
        self.browser.find_element_by_xpath('//*[@id="key"]').send_keys("爬虫书籍")
        self.browser.find_element_by_xpath('//*[@id="search"]/div/div[2]/button').click()
        time.sleep(2)


    def parse_page(self):
        self.browser.execute_script(
            'window.scrollTo(0,document.body.scrollHeight)'
        )
        time.sleep(1)
        li_list=self.browser.find_elements_by_xpath('//*[@id="J_goodsList"]/ul/li')
        for li in li_list:
            li_info = li.text.split('\n')
            if li_info[0][0:2] =="每满":
                price=li_info[1]
                name = li_info[2]
                commit = li_info[3]
                market = li_info[4]

                print([price,name,commit,market])
            else:
                price = li_info[0]
                name = li_info[1]
                commit = li_info[2]
                market = li_info[3]
                print([price, name, commit, market])

    def main(self):
        self.get_page()
        # while True:
        for i in range(1):
            self.parse_page()
            #判断是否该点击下一页
            if self.browser.page_source.find('pn-next disabled')==-1:
                self.browser.find_element_by_class_name('pn-next').click()
                time.sleep(2)
            else:
                break


if __name__ == '__main__':
    spider=JdSpider()
    spider.main()