# polymorphism mean you can use the same function in different signature
# here len can be work as polymorphism bcz same func use in different way
# built in 
a="string"
l=[1,2,2,3,4,4]
print(len(a))
print(len(l))
# user_define
def add(x,y):
    return x+y
print(add(2,3))

#polymorphism in class
class pak:
    def language(self):
        return f"Urdu is national Language of pakistan"
    def animal(self):
        return f"Markhor is the national animal of pakistan"
    def dress(self):
        return f"Shalwar kameez is the national dress"
class india:
    def language(self):
        return f"Hindi is national Language of india"
    def animal(self):
        return f"cow is the national animal of india"
    def dress(self):
        return f"Saree is the national dress"
class US:
    def language(self):
        return f"English is national Language of us"
    def animal(self):
        return f"Sparrow is the national animal of us"
    def dress(self):
        return f"Shirts is the national dress"
    
p=pak()
i=india()
u=US()
for i in (p,i,u):
   print(i.language())
   print(i.animal()) 
   print(i.dress()) 
        


