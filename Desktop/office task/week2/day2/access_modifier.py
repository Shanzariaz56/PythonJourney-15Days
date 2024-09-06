# access modifier means you can access variable of class in three ways
# private (that cannnot be acces outside the class)
# public (that is is normal and can be acces outside the class)
# protected (that cannot ba access outside the class just access within or subclass)
class access_modifier:
    def __init__(self):
        pass
    def public(self):
        print("Pulic Access modifier")
    def _protected(self):
        print("protected access modifier")
    def __private(self):
        print("private access modifier")
        
a=access_modifier()
print(a.public()) 
print(a._protected())
print(a._access_modifier__private())
        