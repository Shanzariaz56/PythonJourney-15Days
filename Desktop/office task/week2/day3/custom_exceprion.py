# custom exception 
class invalidage(Exception):
    def __init__(self,age,message="age must be between 18 and 100"):
        self.age=age
        self.message=message
        super().__init__(message)
def set_age(age):
    if age<18 or age>100:
        raise invalidage(age)
    print(f"you may enter the age:{age}")
try:
    x=int(input("enter the age:::"))
    set_age(x)
except invalidage as e:
    print(f"Invalid age: {e.age}. {e.message}")