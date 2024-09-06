#basics of class
"""class my:
    name="shanza"
    def function(self):
        print(f"my name is {self.name}")
myclass=my()
print(myclass)
print(myclass.function())
class std:
    name="shanzy"
    age=21
    address="vehari"
print(std.name)  #cal class variables
#class base constructor base.....
class std:
    def __init__(self,name,age,grade,address):
        self.name=name
        self.age=age
        self.grade=grade
        self.address=address
    def display(self):
        print(f"Myself {self.name} and am {self.age} years olds and am from {self.address}")
        
# create an object of class
student=std("shanza",20,3.85,"vehari")

#accessing attributes
print(student.name)
print(student.age)
print(student.grade)
print(student.address)

#calling method
print(student.display())"""

#example program,....
#make two function one can take data and other one can display data
class employee:
    def putdata(self):
        self.id=int(input("enter the employee id:"))
        self.name=input("enter the name:")
        self.salary=int(input("enter the salary:"))
    def display(self):
        print("employee id:",self.id)
        print("employee name:",self.name)
        print("employee salary:",self.salary)
emp=employee()
emp.putdata()
emp.display()



