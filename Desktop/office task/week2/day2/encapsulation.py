# provide access to all the variables and method through access modifier
# puting all the things in a box and access can be according to the access modifier
class std:
    def __init__(self,name="shanzy",age=21):
        self.__name=name
        self.__age=age
    def display(self):
        print(f"myself {self.__name} and am {self.__age} years old")
        
s1=std()
s2=std("shanza",20)
s1.display()
s2.display()
# cannot be access because all these variable are private
print(f"myself {s1.__name} and am {s1.__age} years old")
# it can be access only with the class name like that
print(f"myself {s1._std__name} and am {s2._std__age} years old")

        