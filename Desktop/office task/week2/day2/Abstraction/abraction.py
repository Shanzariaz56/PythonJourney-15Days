# abstraction can be implement by abstract class and abstract method
# abstract method can be contain only the definition of the things 
# abstract class can also contain abstract method and concrete method

# simple abstract method ...

from abc import ABC, abstractmethod
#abstract method
class car:
    def __init__(self):
        pass
    @abstractmethod
    def start(self):
        pass
    @abstractmethod
    def stop(self):
        pass

#concrete class
class bike(car):
    def __init__(self):
        pass
    def start(self):
        print("bike is start to kick")   
    def stop(self):
        print("brake is used to stop") 
class motor(car):
    def __init__(self):
        pass
    def start(self):
        print("motor is start to ...")   
    def stop(self):
        print("... is used to stop") 
        
obj=[bike(),motor()]
for i in obj:
    print(i.start())
    print(i.stop())
    

