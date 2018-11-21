class Dog:
    """一次模拟小狗的简单尝试"""
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def sit(self):
        """模拟小狗被命令蹲下"""
        print(self.name.title()+"is now sitting.")

    def roll_over(self):
        """模拟小狗被命令时打滚"""
        print(self.name.title()+"roller over!")


my_dog=Dog('willie',6)

print("My dog's name is "+my_dog.name.title()+".")
print("My dog's name is "+str(my_dog.age)+"years old")