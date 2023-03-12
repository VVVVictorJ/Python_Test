class Mymeta(type):

    def __init__(self, class_name, class_bases, class_dic):
        super(Mymeta, self).__init__(class_name, class_bases, class_dic)

        if class_name.islower():
            raise TypeError('类名 {} 请修改为驼峰体'.format(class_name))

        if '__doc__' not in class_dic or len(
                class_dic['__doc__'].strip('\n')) == 0:
            raise TypeError('类中必须有文档注释，并且文档注释不能为空')


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

