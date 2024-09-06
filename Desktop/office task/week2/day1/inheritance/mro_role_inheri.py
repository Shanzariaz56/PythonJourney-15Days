# super > follow > MRO
# when you can creat the super constructor it can call only the constructor of forst class
# if you have two class and in 3rd class when you can call the both uper class constructor
# if you can call by super so super can call only constructor of first class and other can be call by class name
class A:
    def _init_(self, name):
        self.name = name
    def a_m(self):
        return "that is the 1st Class"
class B(A):
    def _init_(self, name, address):
        super()._init_(name)
        self.address = address
    def b_m(self):
        return "this is the 2nd class"
class C(B):
    def _init_(self, name, address, grade):
        super()._init_(name, address)
        self.grade = grade
    def c_m(self):
        return "this is the 3rd method"
class D(C):
    def _init_(self, name, address, grade, sec):
        super()._init_(name, address, grade)
        self.sec = sec
    def d_m(self):
        return "this is the 4th method"

d = D("shanzy", "vehari", 3.85, "A")
print(d.d_m())
print(d.c_m())
print(d.a_m())
print(d.b_m())