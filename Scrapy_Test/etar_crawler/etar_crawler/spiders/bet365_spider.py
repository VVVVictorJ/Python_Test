# -*- coding: utf-8 -*-
import pandas as pd
from bs4 import BeautifulSoup
from scrapy import Request,Spider
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import scrapy


class Bet365SpiderSpider(scrapy.Spider):
    name = 'bet365_spider'
    allowed_domains = ['https://www.0919365.com/hg_sports/index/fu/ds']
    start_urls = ['https://www.0919365.com/hg_sports/index/fu/ds_page-1-335_',
                  'https://www.0919365.com/hg_sports/index/fu/ds_page-2-335_',
                  'https://www.0919365.com/hg_sports/index/fu/ds_page-3-335_',
                 ]

    def __init__(self):
        '''
        初始化
        :param response:
        :return:
        '''
        chrome_options = Options()
        chrome_options.add_argument('headless')
        chrome_options.add_argument('--disable-gpu')
        # chrome_options=webdriver.ChromeOptions()
        chrome_options.add_argument('--proxy-sever=http://221.7.255.167:8080')
        self.driver = webdriver.Chrome(chrome_options=chrome_options)

    def start_requests(self):
        '''
        提取表格
        :param response:Reponse对象
        :return:
        '''
        for i in range(len(self.start_urls)):
            uurl=self.start_urls[i]
            yield Request(url=uurl,callback=self.parse,meta={'page':i},dont_filter=True)
            #迭代器

    def parse(self, response):
        soup=BeautifulSoup(response,'lxml')#response对象解析成lxml
        table = soup.find_all('table')[0]#find_all直接找table,返回第一个
        df = pd.read_html(str(table))[0]#pandas.read_html直接解析获得表格
        yield df#返回df

    def closed(self,reason):
        #关闭driver对象
        self.driver.quit()



















