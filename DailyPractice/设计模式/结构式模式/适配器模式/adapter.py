class OldCourse:
    """
    老的课程类
    """

    def show(self):
        """
        显示关于本课程的所有信息
        """
        print("Show description")
        print("Show teacher of course")
        print("Show labs")


class Page:
    """
    使用课程对象的客户端
    """

    def __init__(self, course):
        self.course = course

    def render(self):
        self.course.show()


class NewCourse:
    """
    新的课程类，为了模块化显示课程信息，实现了新的课程类
    """

    def show_desc(self):
        """
        显示描述信息
        """
        print("show description")

    def show_teacher(self):
        """
        显示老师信息
        """
        print("Show teacher of course")

    def show_labs(self):
        """
        显示实验
        """
        print("Show labs")


class Adapter:
    """
    适配器，尽管 实现了新的课程类， 但是在很多代码中还是需要使用OldCourse.show()方法
    """

    def __init__(self, course):
        self.course = course

    def show(self):
        """
        适配方法，调用真正的操作
        """
        self.course.show_desc()
        self.course.show_teacher()
        self.course.show_labs()


if __name__ == '__main__':
    old_course = OldCourse()
    page = Page(old_course)
    page.render()
    print('---------------------------------')
    new_course = NewCourse()
    # 新课程类的实例没有 show方法，我们需要使用适配器进行适配
    adapter = Adapter(new_course)
    page = Page(adapter)
    page.render()