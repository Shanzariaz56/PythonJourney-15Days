# in method overriding same name and same arguments
#mostly used for memory reducing process
class area:
    def __init__(self):
        pass
    def calculate(self,a,b):
        print("area will be:",a*b)
class circule(area):
    def __init__(self):
        pass
    def calculate(self,a,b):
        print("area will be:",3.14*a*b)
        
c=circule()
print(c.calculate(10,20))