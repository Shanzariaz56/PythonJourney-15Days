# that is the multiple inheritance
class Uni:
    def __init__(self,name):
        self.name=name
    def display(self):
        return f" the name of uni {self.name} "
    
class Dep:
    def __init__(self,dep):
        self.dep=dep
    def display(self):
        return f" the name of our dep {self.dep}"
    
class std(Uni,Dep):
    def __init__(self,name,dep,sec):
        Uni.__init__(self, name)  
        Dep.__init__(self, dep)   
        self.sec = sec
    def display(self):
        return f" the name of uni {self.name} and department {self.dep} and section {self.sec}"
    
student=std("comsats","cs","batch-23-A")
print(student.display())


#another example of multiplr inheritance
class div:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def divide(self):
        return self.a / self.b
class mod:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def modulus(self):
        return self.a%self.b
    
class div_mod(div,mod):
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def div_mod(self):
        div_value=div.divide(self)
        mod_value=mod.modulus(self)
        return (div_value,mod_value)

calculation=div_mod(10,3)
print("division:",calculation.divide())
print("modulus:",calculation.modulus())
print("division_modulus",calculation.div_mod())

#make a calculator simple multiple inheritance
class add:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def addition(self):
        return self.a+self.b
    
class sub:
    def __init__(self,a,b):
        self.a=a 
        self.b=b
    def subtract(self):
        return self.a-self.b
class mul:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def multiply(self):
        return self.a*self.b
class div:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def divide(self):
        return self.a / self.b
class mod:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def modulus(self):
        return self.a%self.b
    
class calculation(add,sub,mul,div,mod):
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def display(self):
        a=add.addition(self)
        s=sub.subtract(self)
        m=mul.multiply(self)
        d=div.divide(self)
        mo=mod.modulus(self)
        return(a,s,m,d,mo)
        
res=calculation(10,3)
print(res.display())
