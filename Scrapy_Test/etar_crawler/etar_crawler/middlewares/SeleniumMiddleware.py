from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from scrapy.http import HtmlResponse
from logging import getLogger

class SeleniumMiddleware():
    def __init__(self,timeout=None,service_args=[]):
        self.logger=getLogger(__name__)
        self.timeout=timeout
        chrome_options = Options()
        chrome_options.add_argument('headless')
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--proxy-sever=http://221.7.255.167:8080')
        self.driver = webdriver.Chrome(chrome_options=chrome_options)
        self.browser.set_window_size(1400, 700)
        self.browser.set_page_load_timeout(self.timeout)
        self.wait = WebDriverWait(self.browser, self.timeout)

    def __del__(self):
        self.browser.close()

    def process_request(self,request,spider):
        '''
        用chrome抓取页面
        :param request:Request对象
        :param spider:Spider对象
        :return:HtmlResponse
        '''

        self.logger.debug('Chrome is starting')
        #page = request.meta.get('page', 1)
        #这里后面最好加个异常判断

        self.browser.get(request.url)

        return HtmlResponse(url=request.url,body=self.browser.page_source,request=request,encoding='utf-8',status=200)

    @classmethod
    def from_crawler(cls,crawler):
        return cls(timeout=crawler.settings.get('SELENIUM_TIMEOUT')),
        service_args=crawler.settings.get('CHROME-SERVICES-ARGS')
























