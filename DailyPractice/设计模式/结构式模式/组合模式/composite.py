import abc


class Worker:
    """
    工作者抽象类
    """
    __metaclass__ = abc.ABCMeta

    def __init__(self, name):
        self.name = name
    
    @abc.abstractclassmethod
    def work(self):
        pass


class Employee(Worker):
    """
    员工类
    """

    def work(self):
        print("Employee: {} start to work".format(self.name))


class Leader(Worker):
    """
    领导类
    """

    def __init__(self, name):
        super().__init__(name)
        self.members=[]
    
    def add_member(self, employee):
        if employee not in self.members:
            self.members.append(employee)
    
    def remove_member(self, employee):
        if employee in self.members:
            self.members.remove(employee)
    
    def work(self):
        print("Leader: {} start to work".format(self.name))
        for employee in self.members:
            employee.work()


if __name__ == '__main__':
    employee1 = Employee("employee_1")
    employee2 = Employee("employee_2")
    leader_1 = Leader("leader_1")
    leader_1.add_member(employee1)
    leader_1.add_member(employee2)

    employee3 = Employee("employee_3")
    leader_2 = Leader("leader_2")
    leader_2.add_member(employee3)
    leader_2.add_member(leader_1)
    leader_2.work()