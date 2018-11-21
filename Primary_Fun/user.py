class User:
    def __init__(self,first_name,last_name,sex):
        self.first_name=first_name
        self.last_name=last_name
        self.sex=sex
    def describle_user(self):
        print("first name is "+self.first_name)
        print("\t second name is "+self.last_name)
        print("\t sex is "+self.sex)
    def greet_user(self):
        print(self.first_name+" "+self.last_name+"\t你好")
user_1=User('Victor','Robin','man')
user_2=User('Victor','Robben','man')
user_3=User('Victor','Van','man')
List=[user_1,user_2,user_3]
for user in List:
    print(user.describle_user())
    print(user.greet_user())
