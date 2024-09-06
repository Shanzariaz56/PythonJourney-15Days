class std:
    name="shanza"
    age=20
#constructor....
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
#instance method..
    def instace_method(self):
        print(f"myself {self.name} and age {self.age}")
#class method      
    def class_method(cls):
        print(f"myself {cls.name} and age {cls.age}")
#static method     
    def static_method():
        print("this is static method")
        
student=std("shanzyyyy",21)
print(student.instace_method())
print(student.class_method())
print(student.static_method())