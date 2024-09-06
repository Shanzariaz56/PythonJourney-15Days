 # in can only define method and use it in futher concrete class
from abc import ABC, abstractmethod

class Polygon(ABC):
    @abstractmethod
    def noofsides(self):
        pass
class Triangle(Polygon):
    def noofsides(self):
        print("I have 3 sides")
class Pentagon(Polygon):
    def noofsides(self):
        print("I have 5 sides")
class Hexagon(Polygon):
    def noofsides(self):
        print("I have 6 sides")
class Quadrilateral(Polygon):
    def noofsides(self):
        print("I have 4 sides")
s=[Triangle(),Pentagon(),Hexagon(),Quadrilateral()]
for i in s:
    print(i.noofsides())