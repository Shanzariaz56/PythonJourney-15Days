#mutlilevel inheritance
# it work like a grandparent-parent-child like that work
class uni:
    def __init__(self,name):
        self.name=name
    def display(self):
        return f" name of my uni {self.name}"
    
class dep(uni):
    def __init__(self,name,dep_name):
        super().__init__(name)
        self.dep_name=dep_name
    def display(self):
        return f" name of my uni {self.name} and dep {self.dep_name}"
    
class std(dep):
    def __init__(self,name,dep_name,std_name):
        super().__init__(name,dep_name)
        self.std_name=std_name
    def display(self):
        return f"name of uni is {self.name} and dep {self.dep_name} and student {self.std_name}"
    
student=std("comsats","CS","shanzy")
print(student.display())