class Mymeta(type):

    def __call__(self, *args, **kwargs):
        obj = self.__new__(
            self)  # 此处的self是类MyTeacher，必须传参，代表创建一个MyTeacher的对象obj
        self.__init__(obj, *args, **kwargs)  # 2. 调用__init__初始化空对象obj
        obj.__dict__ = {
            '_{}__{}'.format(self.__name__, k): v
            for k, v in obj.__dict__.items()
        }  
        #3. 返回初始化好的对象obj
        return obj


class MyTeacher(object, metaclass=Mymeta):
    """
    类MyTeacher的文档注释
    """
    school = 'john'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say(self):
        print('{} is my name'.format(self.name))


t1 = MyTeacher('zhangsan', 18)
print(t1.__dict__)  # 123