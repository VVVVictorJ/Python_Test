import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from sqlalchemy import create_engine
from openpyxl.workbook import Workbook
import pymysql

#db
connect=create_engine('mysql+pymysql://root:root@localhost:3306/rate?charset=utf8')
#db

chrome_options=Options()
chrome_options.add_argument('headless')
chrome_options.add_argument('--disable-gpu')
# chrome_options=webdriver.ChromeOptions()
chrome_options.add_argument('--proxy-sever=http://221.7.255.167:8080')
driver = webdriver.Chrome(chrome_options=chrome_options)

browser = webdriver.Chrome()

browser.get("https://789666365.com/sport/19#")

soup=BeautifulSoup(browser.page_source,'lxml')

table=soup.find_all('table')[0]
df=pd.read_html(str(table))[0]
df.fillna(0)
df.to_excel('./rate3.xlsx')
browser.quit()
print(df)