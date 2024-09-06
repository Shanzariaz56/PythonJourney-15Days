# hybrid inheritance...
class ceo:
    def __init__(self):
        pass
    def c_m(self):
        return "hlo i am ceo"
class manager(ceo):
    def __init__(self):
        super().__init__()  
        pass
    def m_m(self):
        return "hlo i am manager"
class emp1(manager):
    def __init__(self):
        super().__init__()  
        pass
    def e1_m(self):
        return "hlo am the 1st empployee"
class emp2(manager,ceo):
    def __init__(self):
        super().__init__()  
        pass
    def e2_m(self):
        return "hlo i am 2nd employee"
employee=emp2()
print(employee.c_m())
print(employee.m_m())
print(emp2.e2_m())
        