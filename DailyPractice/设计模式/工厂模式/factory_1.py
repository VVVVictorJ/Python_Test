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


class SimpleCourseFactory:
    """
    简单工厂，用于创建课程
    """

    @staticmethod
    def create_course(course_type, course_name):
        if course_type == 'bc':
            return BasicCourse(course_name)
        elif course_type == 'pc':
            return ProjectCourse(course_name)


if __name__ == '__main__':
    course1 = SimpleCourseFactory.create_course('bc', 'Linux基础入门')
    print(course1.get_labs())
    course2 = SimpleCourseFactory.create_course('pc', 'Python设计模式')
    print(course2.get_labs())
