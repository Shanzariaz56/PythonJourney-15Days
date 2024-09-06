#multiple constructor 
#it can be used when user can nerver know how many arguments can be passed
class student:
    def __init__(self, *args):
        if len(args)==1:
            self.name=args[0]
        elif len(args)==2:
            self.name=args[0]
            self.age=args[1]
        elif len(args)==3:
            self.name=args[0]
            self.age=args[1]
            self.grade=args[2]
            
s1=student("shaanza")
print("name:",s1.name)
s2=student("shanzy",20)
print(f"name of student{s2.name} anf age {s2.age}")
s3=student("shanzy",20,3.84)
print(f"name of student{s3.name} age is {s3.age} and garde {s3.grade}")