metaflyweight = lambda name, parents, attrs: type(
    name, parents,
    dict(
        list(attrs.items()) +
        [('__instances', dict()),
         ('__new__',
          classmethod(lambda cls, *args, **kwargs: cls.__instances.setdefault(
              (args, tuple(kwargs.items())),
              super(type(cls), cls).__new__(cls))))]))


class Spam(object, metaclass=metaflyweight):

    def __init__(self, a, b):
        self.a = a
        self.b = b


class Egg(object, metaclass=metaflyweight):

    def __init__(self, x, y):
        self.x = x
        self.y = y


if __name__ == '__main__':
    # assert Spam(1, 2) is Spam(1, 3)
    # assert Egg('a', 'b') is Egg('a', 'b')
    # assert Spam(1, 2) is not Egg(1, 2)

    spam1 = Spam(1, 2)
    spam2 = Spam(1, 2)
    #spam2 = Spam(1, 3)

    print(id(metaflyweight))
    print(id(spam1))
    print(id(spam2))
    print(spam1 is spam2)
    print(Egg('a', 'b') is Egg('a', 'c'))
    print(spam1.__getattribute__('a'))
    print(spam1.__getattribute__('b'))
    print(spam2.__getattribute__('a'))
    print(spam2.__getattribute__('b'))
