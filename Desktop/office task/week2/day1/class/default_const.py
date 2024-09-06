class myclass:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print(f"name is {self.name} and age is {self.age}")
a=myclass("shanza",20)
#accessing attributes
print(a.name)
print(a.age)
#modifying attributes
a1=myclass("shanzyyy",21)
print(a1.name)
print(a.age)
#built_in attributes(in built in we can use classname.attribute name)
print(myclass.__bases__)
print(myclass.__dict__)
print(myclass.__annotations__)
print(myclass.__name__)
print(myclass.__module__)

#default constructor....
class Dog:
    def __init__(self, name="Unknown", age=0):
        self.name = name
        self.age = age

# Creating an object without passing arguments
stray_dog = Dog("harry",20)
print(stray_dog.name)  # Output: Unknown
print(stray_dog.age)  

#default constructor can be used when you can set already a value but usse can change it when it can want