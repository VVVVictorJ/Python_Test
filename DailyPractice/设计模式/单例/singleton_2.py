class SingletonDeco:
    """
    单例装饰器
    """

    def __init__(self, cls):
        self._cls = cls

    def instance(self):
        try:
            return self._instance
        except AttributeError:
            self._instance = self._cls()
        return self._instance

    def __call__(self):
        return self.instance()


@SingletonDeco
class Singleton:

    def display(self):
        return "{}:".format(__class__.__name__) + str(id(self))


if __name__ == '__main__':
    s1 = Singleton()
    s2 = Singleton()
    print('id(s1): ', s1.display())
    print('id(s2): ', s2.display())
    print('s1 is s2', s1 is s2)