import logging


class AutoFormatSqlGenarator:
    def __init__(self, FormatTemplateStr: str) -> None:
        self.FormatTemplateStr = FormatTemplateStr

    def GenFormatString(self, param) -> str:
        for k, v in param:
            print(self.FormatTemplateStr.format())
        return

    @staticmethod
    def Test():
        exec('print("Hello")')


if __name__ == "__main__":
    AutoFormatSqlGenarator.Test()
    table = {"Sjoerd": 4127, "Jack": 4098, "Dcab": 8637678}
    print(
        "Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; " "Dcab: {0[Dcab]:d}".format(table)
    )
    tmp = {"a": 123}
    print(
        "1:{0[a]:d}".format(tmp)
    )