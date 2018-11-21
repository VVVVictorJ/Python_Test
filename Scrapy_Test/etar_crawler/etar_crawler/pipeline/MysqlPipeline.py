import pymysql

class MysqlPipeline(object):
    def __init__(self):
        self.client=pymysql.connect(
            host='127.0.0.1',
            port='3306',
            user='root',
            passwd='123456',
            db='scrapy',
            charset='utf8'
        )
        self.cur=self.client.cursor()
    #没写完
