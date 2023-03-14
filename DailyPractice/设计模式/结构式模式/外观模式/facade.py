class User:
    """
    用户类
    """

    def is_login(self):
        return True

    def has_privilege(self, privilege):
        return True


class Course:
    """
    课程类
    """

    def can_be_learned(self):
        return True


class Lab:
    """
    实验类
    """

    def can_be_started(self):
        return True


# 创建客户端类，该类的实例用来启动实验环境。启动实验环境前，先要对用户，课程和实验进行判断，全部符合要求才会启动实验环境
class Client:
    """
    客户类，用于开始一个实验
    """

    def __init__(self, user, course, lab):
        self.user = user
        self.course = course
        self.lab = lab

    def start_lab(self):
        """
        开始实验，需要一系列的判断：
        用户是否登录，课程是否学习，实验是否可以开始。判断非常繁琐
        """
        if (self.user.is_login() and self.course.can_be_learned()
                and self.lab.can_be_started()):
            print("Start lab")
        else:
            print("Can not start lab")


class FacadeLab:
    """
    新的Lab类,应用了面向对象模式
    """

    def __init__(self, user, course, lab):
        self.user = user
        self.course = course
        self.lab = lab

    def can_be_started(self):
        if (self.user.is_login() and self.course.can_be_learned()
                and self.lab.can_be_started()):
            return True
        else:
            return False
        

class NewClient:
    """
    新的客户类，使用外观模式
    """
    def __init__(self, facade_lab):
        self.lab = facade_lab
    
    def start_lab(self):
        """
        开始实验，只需要判断FacadeLab是否可以开始
        """
        if self.lab.can_be_started:
            print("Start lab")
        else:
            print("Can not start lab")

if __name__ == '__main__':
    print('General Pattern:')
    user = User()
    course = Course()
    lab = Lab()
    client = Client(user, course, lab)
    client.start_lab()

    print("Facade Pattern:")
    facade_lab = FacadeLab(user, course, lab)
    facade_client = NewClient(facade_lab)
    facade_client.start_lab()