#built in function that can be directly used without any declaration
l1=[1,2,3,3,4,4,5,5]
print(len(l1))

#upercase
l1=["shanza","riaz","talha"]
uper_case= [i.upper() for i in l1]
print(uper_case)

#lowercase
l1=["SHANZA","RIAZ"]
lower=[i.lower() for i in l1]
print(lower)

import math
x=int(input("enter the number::"))
y=int(input("enter the number::"))
#Arithmetic and Exponential Functions
print(math.sqrt(x))   #square root
print(math.pow(x,y))  #power 
print(math.log(100,10))

#rounding and absolute function
print(math.fabs(x))
print(math.ceil(5.6)) #round off the value in greater
print(math.floor(4.2)) #round off the value in less

#trignometric function
x1=float(input("enter the number"))
print(math.degrees(x1))
print(math.sin(x))
print(math.cos(x))
print(math.tan(x))
print(math.cos(math.pi/2))
print(math.sin(math.pi/2))
print(math.tan(math.pi/2))
print(math.radians(x))

#Factorial and Combinatorial 
n=int(input("number of total items:"))
k=int(input("number of items want to choose:"))
print(math.factorial(x))
print(math.comb(n,k))

from datetime import date
print(date.today())
# for day
d=date(2024,8,19)
print(d.day)
#convert seconds into the date like UTC
timestamp=1567890890    #seconds
d=date.fromtimestamp(timestamp) #convert into date
print(d)

#fromordinal can be used that can show interger 
#means no.of days from that date
ordinal=1  #no of days
d=date.fromordinal(ordinal) #convert into date
print(d)

#replace values
old_date=date(2004,2,9)
new_date=old_date.replace(2024,8,9)
print(old_date)
print(new_date)

d1=date(2002,9,8)
d2=date(2024,8,19)
#weekday where 0 is monday
print(d2.weekday())
#isoweekday where monaday start 1
print(d2.isoweekday())
#isoformat where date can be return in a format
print(d1.isoformat())
#string representing date in format
print(d1.ctime())
#equal to other date
print(d1.__eq__(d2))
#not equal
print(d1.__ne__(d2))
#less than other
print(d1.__lt__(d2))
#less tha or equal
print(d1.__le__(d2))
#greater than
print(d1.__gt__(d2))
print(d1.__ge__(d2))


#os module....
#os module can be used for interacting with operating system
#in which you can gave directory path like that thing
import os
print("current director:",os.getcwd())
#print("change director:",os.chdir())
print("new director:",os.mkdir("new_folder"))
print("remove director:",os.rmdir("new folder"))
