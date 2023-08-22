import os
import logging
import datetime

class Log(object):
    '''
    封装后的logging
    '''

    def __init__(self, logger=None, logpath=None):
        '''
            指定保存日志的文件路径，日志级别以及调用文件
            将日志存入到指定的文件中
        '''

        # 创建一个logger
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.INFO)
        # 创建一个handler，用于写入日志文件
        self.log_time = datetime.datetime.now().strftime("%Y-%m-%d")
        if not os.path.exists(logpath):
            os.makedirs(logpath)
        self.log_name = os.path.join(logpath, f"AutoImport_log_{self.log_time}.log")

        fh = logging.FileHandler(self.log_name, mode='a', encoding='utf-8')
        fh.setLevel(logging.INFO)

        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)

        formatter = logging.Formatter(
            '[%(asctime)s] [%(name)s - %(levelname)s] %(filename)s->%(funcName)s [line:%(lineno)d]: %(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        self.logger.addHandler(fh)
        self.logger.addHandler(ch)

        fh.close()
        ch.close()

    def getlog(self):
        return self.logger












