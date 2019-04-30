# coding=utf-8
from lxml import etree

html=""

# parseHtml=etree.HTML(html)
# r1=parseHtml.xpath("//a/text()")
parseHtml=etree.HTML(html)
r2=parseHtml.xpath("//a/@href")

r3=parseHtml.xpath("//div[@class='wrapper']/ul//a/@href")

r4=parseHtml.xpath("//a/text()")

r5=parseHtml.xpath("//div[@class='wrapper']/ul//a/text")
