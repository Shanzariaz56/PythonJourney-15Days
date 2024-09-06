# overloading is a concept of polymorohism
#it is worked in the same function name but different arguments
class area:
    def __init__(self):
        pass
    def calculation(self,a=None,b=None):
        if a!=None and b!=None:
            print("the calculation of area:",a*b)
        elif a!=None:
            print("the calculation of area:",a*a)
        else:
            print("Kuch niiiiiiiiiiii")
            
a=area()
print(a.calculation(10,20))
print(a.calculation(10))
print(a.calculation())