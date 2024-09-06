class vehicle:
    def __init__(self,name,model,year):
        self.name=name
        self.model=model
        self.year=year
    def display(self):
        print(f"Name of vehicle {self.name} and its model {self.model} and year {self.year}")
class car(vehicle):
    def __init__(self,name,model,year,color):
        super().__init__(name,model,year)
        self.color=color
    def display(self):
        super().display()
        print(f"Color : {self.color}")
class truck(vehicle):
    def __init__(self,name,model,year,load):
        super().__init__(name,model,year)
        self.load=load
    def display(self):
        super().display()
        print(f"Carry work load: {self.load}")
        
c=car("Toyotta","corolla",2024,"black")
print(c.display())
t=truck("heavy","normal",2021,500)
print(t.display())
        