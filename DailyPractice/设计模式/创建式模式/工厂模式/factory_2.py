import abc


class Factory(metaclass=abc.ABCMeta):
    """
    抽象工厂类
    """

    @abc.abstractclassmethod
    def create_course(self):
        pass


class BasicCourseFactory(Factory):
    """
    基础课程工厂类
    """

    @classmethod
    def create_course(cls, course_name):
        return BasicCourse(course_name)


class ProjectCourseFactory:
    """
    项目课程工厂类
    """

    @classmethod
    def create_course(cls, course_name):
        return ProjectCourse(course_name)


class BasicCourse:
    """
    基础课程
    """

    def __init__(self, course_name):
        self.course_name = course_name

    def get_labs(self):
        return "基础课程《{}》的实验列表...".format(self.course_name)

    def __str__(self):
        return "BasicCourse"


class ProjectCourse:
    """
    项目课程
    """

    def __init__(self, course_name):
        self.course_name = course_name

    def get_labs(self):
        return "项目课程《{}》的实验列表...".format(self.course_name)

    def __str__(self):
        return "ProjectCourse"


if __name__ == '__main__':
    course1 = BasicCourseFactory.create_course('Linux基础入门')
    print(course1.get_labs())
    course2 = ProjectCourseFactory.create_course('Python 设计模式')
    print(course2.get_labs())