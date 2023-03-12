class Singleton:
    '''
    单例模式
    '''

    class _A:

        # 返回嵌套类的实例的内存地址
        def display(self):
            return id(self)

    _instance = None

    # 创建Singleton类的实例后，执行此方法。方法内部是对类的操作，为类的_instance属性赋予一个_A的实例。第一次对Singleton进行实例化时会创建一个_A类的实例并赋值，以后不再变化。
    def __init__(self) :
        __class__._instance = __class__._instance or __class__._A()

    # Singleton 类内部故意不为自身的实例设置任何属性，结果就是调用实例的属性时最后落到此方法的头上。方法内部获取类属性 _instance 的同名属性，也就是 _A 类的实例的属性。
    def __getattr__(self, attr):
        return getattr(__class__._instance, attr)

    # 此方法内部调用 object.__setattr__ 方法为 Singleton._instance 也就是 _A 的实例定义属性。
    def __setattr__(self, attr, value):
        object.__setattr__(__class__._instance, attr, value)


if __name__ == '__main__':
    s1 = Singleton()
    s2 = Singleton()

    print('id(s1):', id(s1))
    print('id(s2):', id(s2))

    print('s1.display():', s1.display())
    print('s2.display():', s2.display())

    s1.name = 'James'
    print('s1.name:', s1.name)
    print('s2.name:', s2.name)

    # Singleton 的实例各不相同，它们在赋值属性和调用属性时，结果却是相同的。因为这些实例操作属性时都转移到了嵌套类 _A 的实例上。
    # id(s1): 1529782893872
    # id(s2): 1529782893776
    # s1.display(): 1529782893824
    # s2.display(): 1529782893824
    # s1.name: James
    # s2.name: James