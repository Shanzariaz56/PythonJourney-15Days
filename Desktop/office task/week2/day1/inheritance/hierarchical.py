# that is the hieracrchical inheritance
# in which one is main/parent class and other subclass are inherit to it
class manager:
    def __init__(self):
        pass
    def manage(self):
        return "hi! Am the manager. Welcome to the party"
class senior_emp(manager):
    def __init__(self):
        pass
    def sen_emp(self):
        return "WELCOME Jerry >> AM senior employee"
class junior_emp(manager):
    def __init__(self):
        pass
    def jun_Emp(self):
        return "Abyy &&  AM junior Ghost huhhhhhh"
    
emp1=senior_emp()
print(emp1.manage())
print(emp1.sen_emp())

emp2=junior_emp()
print(emp2.manage())
print(emp2.jun_Emp())