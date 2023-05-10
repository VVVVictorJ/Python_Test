import logging


class AutoFormatSqlGenarator:
    def __init__(self, FormatTemplateStr: str) -> None:
        self.FormatTemplateStr = FormatTemplateStr

    def GenFormatString(self, param: dict) -> str:
        for k, v in param.items():
            print(self.FormatTemplateStr.format(v[0], v[1], v[2], v[3], v[4]))
        return

    @staticmethod
    def Test():
        exec('print("Hello")')


if __name__ == "__main__":
    AutoFormatSqlGenarator.Test()
    # table = {"Sjoerd": 4127, "Jack": 4098, "Dcab": 8637678}
    # print(
    #     "Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; " "Dcab: {0[Dcab]:d}".format(table)
    # )
    # tmp = {1: "123"}
    # print(
    #     "a:{0[1]}".format(tmp)
    # )
