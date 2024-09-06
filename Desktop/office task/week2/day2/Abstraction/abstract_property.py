# when we can use property method so it can treat method as a varibale /attribute
# when we can make a class as an abstarct so we cannot make object of that class
import abc
from abc import ABC ,abstractmethod
class std(ABC):
    def __init__(self):
        pass
    @abc.abstractmethod
    def display(self):
        return "that is abstract method"
class std_child(std):
    def __init__(self):
        pass
    @property
    def display(self):
        return "child class"
    
try:
    s=std()
    print(s.display)
except Exception as err:
    print(err)

c=std_child()
print(c.display)