class Foo(object):

    def __init__(self, func) -> None:
        self._func = func

    def __call__(self):
        print('class decorator runing')
        self._func()
        print('class decorator ending')


@Foo
def bar():
    print('bar')

if __name__ == '__main__':
    bar()