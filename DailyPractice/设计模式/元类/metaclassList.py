class ListMeta(type):

    """
    param:metacls 指代元类本身
    param:cls_name 指代创建的类的类名
    param:super_cls_tuple 就是新建的类需要继承的父类的元组
    param:args_dict 为字典, 有一些key, 例如 __module__, __doc__等

    注意：在我们的元类中定义方法，参数 metacls 通常指代元类本身，参数 cls 指代利用元类定义的类。
    """
    def __new__(metacls, cls_name, super_cls_tuple, args_dict):
        args_dict['add']=lambda self, value:self.append(value)
        return type.__new__(metacls, cls_name, super_cls_tuple, args_dict)
        # a = type.__new__(metacls, cls_name, super_cls_tuple, args_dict)
        # print('-------a 就是 List 类:', a)
        # print('-------List 类的属性:', dir(a))
        # return a
    
    def __init__(cls, name, bases, namespace, **kwargs):
        print('__init__ cls:', cls)
        # 第一次使用 ListMeta 元类创建类 List 时
        # List 没有 sub_class_dict 这个属性，就定义一个空字典给它
        # 使用 List 作为父类创建子类 L1 和 L2 时
        # 子类会继承父类的 sub_class_dict 属性，这由 type.__new__ 完成
        # 继承关系的类们共享父类的属性，除非子类重新定义该属性
        if not hasattr(cls, 'sub_class_dict'):
            cls.sub_class_dict = {}
        else:
            cls.sub_class_dict[name.lower()] = cls
        print('初始化完成\n')

    
class List(list, metaclass=ListMeta):
    '''
    创建 List 类时，会调用元类 ListMeta 的 __new__ 方法
    返回值是调用 type 的 __new__ 方法，该方法会将父类的“非私有属性”赋值给 List 类
    type.__new__ 方法的返回值就是 List 类
    最后再调用 ListMeta.__init__ 方法初始化一下
    '''
    name = 'Helloworld'

if __name__ == '__main__':
    class L1(List): ...
    class L2(List): ...

    print(List.sub_class_dict)
    print(L2.sub_class_dict)

    l = List()
    l.add('age')
    print(l)
    # new_list = list()
    # if hasattr(new_list, 'add'):
    #     print('new_list 有add 属性')