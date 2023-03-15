metaflyweight = lambda name, parents, attrs: type(
    name, parents,
    dict(
        list(attrs.items()) +
        [('__instances', dict()),
         ('__new__',
          classmethod(lambda cls, *args, **kwargs: cls.__instances.setdefault(
              tuple(args),
              super(type(cls), cls).__new__(cls))))]))

print(metaflyweight)


class Spam(object,metaclass=metaflyweight):

    def __init__(self, a, b):
        self.a = a
        self.b = b


class Egg(object):
    __metaclass__ = metaflyweight

    def __init__(self, x, y):
        self.x = x
        self.y = y


assert Spam(1, 2) is Spam(1, 2)
# assert Egg('a', 'b') is Egg('a', 'b')
# assert Spam(1, 2) is not Egg(1, 2)

spam1 = Spam(1, 2)
spam2 = Spam(1, 2)

print(id(spam1))
print(id(spam2))
print(spam1 is spam2)
