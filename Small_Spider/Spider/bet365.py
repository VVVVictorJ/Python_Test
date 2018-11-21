import urllib3
import urllib.request
import re
import os
import urllib

from bs4 import BeautifulSoup
from cssselect import Selector
from selenium import webdriver
import http.cookiejar
from selenium.webdriver.chrome.options import Options
from lxml import etree


def trim(s):
    for i in range(len(s)):
        if s[0] == ' ':
            s = s[1:]
    for k in range(len(s)):
        if s[-1] == ' ':
            s = s[:-1]
    return s

chrome_options=Options()
chrome_options.add_argument('headless')
chrome_options.add_argument('--disable-gpu')
# chrome_options=webdriver.ChromeOptions()
chrome_options.add_argument('--proxy-sever=http://222.184.7.206:40908')
driver = webdriver.Chrome(chrome_options=chrome_options)

browser = webdriver.Chrome()

browser.get("https://789666365.com/sport/19#")


File=open("赔率.txt",'w',encoding='utf-8')

html=etree.HTML(browser.page_source)

# new_html=html.get_text('\n','<br/>')
html_data=html.xpath('//*[@id="sportframe"]')
print(html_data)
# html_data=html.xpath('//*[@id="data"]/tbody//tr//td[@align="left"]')
# html_data=html_data.decode('utf-8')
# for i in range(len(html_data)):
#     if(i%2)==0:
#         # co=re.split(r'\<br\>([\w\/]+)$', html_data[i].text)
#         # print(co)
#         print(html_data[i].xpath('string(.)').strip())
#         File.write(html_data[i].xpath('string(.)').strip()+'\n')
# File.write('\n')
# html_data_1=html.xpath('//*[@id="data"]/tbody/tr//td')
#
# for i in range(len(html_data_1)):
#     if(i%2)==0:
#         s=trim(html_data_1[i].xpath('string(.)'))
#         print(s)
#         File.write(html_data_1[i].xpath('string(.)').lstrip())
        #去除tr之间的br

        # print(html_data[i].attrib)##html_data的属性
        # print(html_data[i].tag)
        # print(type(html_data[i]))##html_data的类型
# print(browser.page_source)

browser.close()


# def getHtml(url):
#     req = urllib.request.Request(url)
#     req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:57.0) '
#                                  'Gecko/20100101 Firefox/57.0')
#     data = urllib.request.urlopen(req).read()
#     return data
#
# html=getHtml("https://www.0919365.com/hg_sports")
#
# print(html)