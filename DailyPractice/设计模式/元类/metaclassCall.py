class NoInstanceMeta(type):
    def __init__(cls, *args, **kwargs):
       print('NoInstanceMeta Creating Spam')

    def __call__(cls, *args, **kwargs):
        raise TypeError('这个类不能实例化')


class NoInstance(metaclass=NoInstanceMeta):
    name = 'Victor'
    def __init__(self):
       print('Creating Spam')
    # self : 表示实例化类后的地址id
    # classmethod 修饰符对应的函数不需要实例化，不需要 self 参数，但第一个参数需要是表示自身类的 cls 参数，可以来调用类的属性，类的方法，实例化对象等。
    @classmethod
    def hello(cls, name):
        print('Hello,', name)

ni = NoInstance()

NoInstance.hello('Kitty')