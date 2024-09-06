#there are basically three main method pf class
#instance method
#class method
#static method 

#first we will discuss about instance method..
#instance method can be created inside a class as a function
class std:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def instance_method(self):
        print(f"myslf {self.name} and age {self.age}")
student=std("shanzy",20)
print(student.instance_method())

#class method are the function that operate on class itself rather that its instance
#also use a decorator
class employee:
    name="shanza"
    age=20
    def __init__(self):
        pass
    @classmethod
    def class_method(cls):
        print(f"myself {cls.name} and age{cls.age}")
        
Employee=employee()
print(Employee.class_method())

#static method are define inside a class but not operate on instance and class itself
#self contain func that belong to class name itself
class car:
    name="honda"
    model=2020
    def __init(self):
        pass
    @staticmethod
    def static_method():
        print("today i miss my family:")
        
print(car.static_method())

# another example of car....
class mycar:
    wheels=4
    #constructor (instance method)
    def __init__(self,name,color,model):
        self.name=name
        self.color=color
        self.model=model
    def instance_method(self):
        print(f"the name of my car{self.name} and its color is {self.color} and its model {self.model}")
    #class method
    @classmethod
    def class_method(cls):
        print(f"the car has tottal wheel {cls.wheels}") 
    #static method
    @staticmethod
    def static_method():
        print("beep beep paaa paaa!!!")
        
Carr=mycar("honda","black",2020)
print(Carr.instance_method())
print(Carr.class_method())
print(Carr.static_method())       
    