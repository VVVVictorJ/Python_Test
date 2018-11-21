import scrapy
from myweb.part12.myfirstpjt.myfirstpjt.items import MyfirstpjtItem
class WeisuenSpider(scrapy.Spider):
    name = "weisuen"
    #allowed_domains=["sina.com.cn"]
    start_urls=(
        'http://slide.news.sina.com.cn/s/slide_1_2841_298211.html#p=1',
        'http://news.sina.com.cn/p1/2016-09-12/doc-ifxvukhv8147404.shtml',
        'http://news.sina.com.cn/gov/xlxw/2018-07-13/doc-ihfhfwmu7650916.shtml',
    )
    urls2=("http://www.jd.com",
           "http://sina.com.cn",
           "http://yum.iqianyue.com",
           )
    def start_requests(self):
        for url in self.urls2:
            yield self.make_requests_from_url(url)
    def parse(self, response):
        item=MyfirstpjtItem()
        item["urlname"]=response.xpath("/html/head/title/text()")
        print(item["urlname"])