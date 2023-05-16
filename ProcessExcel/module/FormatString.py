import logging
from functools import wraps

logging.basicConfig(
    filename="E:\code\Python\ProcessExcel\module\example.log",
    encoding="utf-8",
    level=logging.DEBUG,
)


def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        from time import time

        t_start = time()
        result = func(*args, **kwargs)
        t_end = time()
        # print("time spend: {}".format(t_end - t_start))
        logging.debug("Using Time: {}s".format(t_end - t_start))
        return result

    return wrapper


def log(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        logging.debug("Function {} is running.".format(func.__name__))
        result = func(*args, **kwargs)
        logging.debug("Function {} is finising.\n".format(func.__name__))
        return result

    return wrapper


class AutoFormatSqlGenarator:
    def __init__(self, FormatTemplateStr: str) -> None:
        self.FormatTemplateStr = FormatTemplateStr

    @log
    @timer
    def GenFormatString(self, param: dict) -> str:
        for k, v in param.items():
            print(self.FormatTemplateStr.format(v))
        return

    @staticmethod
    def Test():
        exec('print("Hello")')


# if __name__ == "__main__":
#     AutoFormatSqlGenarator.Test()
# table = {"Sjoerd": 4127, "Jack": 4098, "Dcab": 8637678}
# print(
#     "Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; " "Dcab: {0[Dcab]:d}".format(table)
# )
# tmp = {1: "123", 2:"456"}
# print(
#     "a:{0[1]}, b:{0[2]}".format(tmp)
# )
