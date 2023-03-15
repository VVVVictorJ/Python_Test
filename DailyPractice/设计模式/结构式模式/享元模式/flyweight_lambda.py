metaflyweight = lambda name, parents, attrs: type(
    name, parents,
    dict(list(attrs.items()) +
            [
                ('__instances', dict()),
                ('__new__',
                    classmethod(lambda cls, *args, **kwargs:
                     cls.__instances.setdefault
                        (
                            (args, tuple(kwargs.items())), cls(args, kwargs)
                        )
                    )
                )
            ]
        )
    )

print(metaflyweight)


class Spam(object):

    def __init__(self, a, b):
        self.a = a
        self.b = b
        


class Egg(object):
    __metaclass__ = metaflyweight

    def __init__(self, x, y):
        self.x = x
        self.y = y


# assert Spam(1, 2) is Spam(1, 2)
# assert Egg('a', 'b') is Egg('a', 'b')
# assert Spam(1, 2) is not Egg(1, 2)

spam1 = Spam(1, 2)
spam2 = Spam(1, 2)

print(spam1.__dict__)
print(spam2.__dict__)
# print(id(spam2))


