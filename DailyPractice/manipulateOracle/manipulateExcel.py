import xlrd


class metaManipulateExcel(type):

    def __new__(metacls, cls_name, super_cls_tuple, args_dict):
        # 未创建类时已启用该函数
        print('【metaManipulateExcel】is __new__')
        return type.__new__(metacls, cls_name, super_cls_tuple, args_dict)

    def __init__(cls, *args, **kwargs):
        cls.__instance = None

    def __call__(cls, *args, **kwargs):
        print('【metaManipulateExcel】is __call__')
        if cls.__instance is None:
            for v in args:
                pass
            for k, v in kwargs.items():
                setattr(cls, k, v)
            cls.__instance = super().__call__(*args, **kwargs)
            return cls.__instance
        else:
            return cls.__instance


class manipulateExcel(metaclass=metaManipulateExcel):

    def __init__(self, *args, **kwargs):
        if not hasattr(self, 'filelocation'):
            raise TypeError('Doesn\'t has filelocation attribution.')
        if not hasattr(self, 'sheetNo'):
            raise TypeError('Doesn\'t has sheetNo attribution.')
        self.excelInstance = None
        self.table=None
        return super().__init__()
    
    @classmethod
    def getfilelocation(self):
        print(getattr(self, 'filelocation'))

    def getExcelSheet(self):
        self.excelInstance = xlrd.open_workbook(getattr(self, 'filelocation'))
        self.table = self.excelInstance.sheet()[0]
    
    def getRowData(self):
        pass
        


obj1 = manipulateExcel(filelocation=r'C://desktop')
obj2 = manipulateExcel(filelocation=r'D://code')

# print("id(obj1) is:", id(obj1))
# print("id(obj2) is:", id(obj2))
# print(getattr(obj2, 'filelocation'))
# print("obj1 is obj2:", obj1 is obj2)
obj1.getfilelocation()