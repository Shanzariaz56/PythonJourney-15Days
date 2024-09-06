#inheritance is most important feature of oop
#inheritance can be used to inherit properties and behaviour of one class to another class
# the class that inherit to the previous class is child class
# and the class that can he inherited is parent class

# single inheritance first
class teacher:
    def teachermethod(self):
        print("thats is the parent class:")
class student(teacher):
    def studentmethod(self):
        print("that is the childern class")
        
c=student()
# childern method
print(c.studentmethod())
# parent method
print(c.teachermethod())

#another example of single inheritance
class animal:
    def __init__(self,name):
        self.name=name
    def speak(self):
        return "its sound good"
class Dog(animal):
    def __init__(self,name,color):
        super().__init__(name)
        self.color=color
    def speak(self):
        return "bark bark"
    def display(self):
        return f"the name of dod is {self.name} and its color is {self.color}"
    
mydog=Dog("jack","black")
print(mydog.display())
