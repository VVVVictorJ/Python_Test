import abc


class LinuxVm:
    """
    Linux 虚拟机
    """

    def start(self):
        print("Linux vm running")


class MacVm:
    """
    Mac OSX 虚拟机
    """

    def start(self):
        print("Mac OSX vm running")


class Factory(metaclass=abc.ABCMeta):
    """
    抽象工厂类
    """

    @abc.abstractmethod
    def create_course(self):
        pass

    @abc.abstractmethod
    def create_vm(self):
        pass


class BasicCourseFactory:
    """
    基础课程工厂类
    """

    @classmethod
    def create_course(cls, course_name):
        return BasicCourse(course_name)

    @classmethod
    def create_vm(cls):
        return LinuxVm()


class ProjectCourseFactory:
    """
    项目课程工厂类
    """

    @classmethod
    def create_course(cls, course_name):
        return ProjectCourse(course_name)

    @classmethod
    def create_vm(cls):
        return MacVm()


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
    course1 = BasicCourseFactory.create_course('Linux 基础入门')
    vm1 = BasicCourseFactory.create_vm()
    print(course1.get_labs())
    vm1.start()

    course2 = ProjectCourseFactory.create_course('Python 设计模式')
    vm2 = ProjectCourseFactory.create_vm()
    print(course2.get_labs())
    vm2.start()