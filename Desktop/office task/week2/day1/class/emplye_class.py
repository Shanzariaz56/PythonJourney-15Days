class employee:
    emp_count=0
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
        employee.emp_count+=1
    def count(self):
        print(f"total employee will be {employee.emp_count}")
    def display(self):
        print(f"name of employee {self.name} and its salary {self.salary}")
        
emp1=employee("shanzy",200000)
emp2=employee("shahnaz",40000)
emp1.display()
emp2.display()
print(f"Total employeee {employee.emp_count}")
emp1.age=20
print(emp1.age)