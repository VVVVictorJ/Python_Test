class BaseMeta(type):
    def __new__(metacls, name, bases, namespcace, **kwargs):
        if name != 'Base' and 'bar' not in namespcace:
            raise TypeError('bad user class')
        return super().__new__(metacls, name, bases, namespcace, **kwargs)
    
class Base(object, metaclass=BaseMeta):
    def foo(self):
        return self.bar()
    
if __name__ == '__main__':
    class Base1(Base):
        def bar(self):
            ...
    print('Base1 创建完成')

    class Base2(Base):
        ...
    print('Base2 创建完成')