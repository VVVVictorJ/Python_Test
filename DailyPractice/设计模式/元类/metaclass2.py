class Mymeta(type):

    def __call__(self, *args, **kwargs):
        print(self)  #<class '__main__.MyTeacher'>
        print(args)  #('zhangsan', 18)
        print(kwargs)  #{'x': 1, 'y': 2, 'z': 3}
        return 123


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


t1 = MyTeacher('zhangsan', 18, x=1, y=2, z=3)
print(t1)  # 123