import logging
import os
from functools import wraps

logging.basicConfig(
    filename="example.log",
    encoding="utf-8",
    level=logging.DEBUG,
)


def log(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        logging.debug("Function {} is running.".format(func.__name__))
        result = func(*args, **kwargs)
        logging.debug("Function {} is finising.\n".format(func.__name__))
        return result

    return wrapper


class BackUpToFile:
    def __init__(self) -> None:
        self.resultPath = os.path.sep.join([os.getcwd(), "test.txt"])
        # print(self.resultPath)

    @log
    def ProcessDictToFile(self, param: dict, templateString: str):
        with open(self.resultPath, "w+") as f:
            for k, v in param.items():
                f.write(templateString.format(v) + "\n")


# obj = BackUpToFile()
# obj.ProcessListToFile()
