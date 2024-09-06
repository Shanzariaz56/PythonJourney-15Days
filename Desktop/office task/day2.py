# function can be used for the repetition and function can be call by its aurguments and not by its arguments
#function can be used when we can call a same block of code again and again
#types of function lambda function, recursive function and built in funcion
# function is reusable block of code

#simple function:
from functools import reduce
def function():
    return "hello world!"
print(function())

# for addition
def add(a,b):
    sum=a+b
    return sum
print(add(1,2))

#make a calculator
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
def modulus(a,b):
    return a%b
def calcultor():
    print("Simple Calculator//")
    print("1. select it for Addition")
    print("2. select it for Asubtraction")
    print("3. select it for multiplication")
    print("4. select it for division")
    print("5. select it for Modulus")
    
    choice=int(input("enter your choice"))
    n1=int(input("enter the first number"))
    n2=int(input("enter the second number"))
    
    if(choice==1):
        print(f"Result of Addition: {add(n1,n2)}")
    elif(choice==2):
        print(f"result of subtraction {sub(n1,n2)}")
    elif(choice==3):
        print(f"result of multiplication {mul(n1,n2)}")
    elif(choice==4):
        print(f"result of division {div(n1,n2)}")
    elif(choice==5):
        print(f"result of modulu {modulus(n1,n2)}")
    else:
        print("wrong input")
print(calcultor())

#calculate factorial
def fac(x):
    if x==1:
        return 1
    else:
        return x*fac(x-1)

n=int(input("enter the number you want to take it factorial::"))
print(fac(n))   

#greeting function....
def greet(name):
    print(f"Good Morning {name}")
    
n=input("enter the Name::")    
print(greet(n))

#default arguments
def greet(name="shanzyyyyy"):
    print(f"Good Morning {name}")
     
print(greet())
print(greet("shahnaz"))

# convert Celsius to Fahrenheit
def Celsius_to_Fahrenheit(cel):
    return (cel*9/5)+32

print(Celsius_to_Fahrenheit(25))

#print function
def  custom_print(end=" "):
    pass
    
print(f"shanzy khan {custom_print()}")

#list of benenfits of function....
def list_benefits():
    return "more readable","more efficient", "Easier code reuse", "Allowing programmers to share and connect code together"
def sequence_sentence(benefit):
    return f"{benefit} is benefit of function"
def name_if_benefits():
    list_of_benefits=list_benefits()
    for i in list_of_benefits:
        print(sequence_sentence(i))
        
print(name_if_benefits())

#lambda function......
add=lambda x,y:x+y
print(add(3,5))

square=lambda x:x**2
n=int(input("enter the number:"))
print(square(n))

#map function...
list_number=[1,2,3,4,5,6,7,9,10]
cubes=map(lambda x:x**3, list_number)
print(list(cubes))

#for square....
numbers=[2,3,4,5,6,7,8]
square=map(lambda x:x**2,numbers)
print(list(square))

#convert into upperr case...
name_list=["shanza","saira","talha","ali","abdullah"]
uper_case=map(lambda word:word.upper(),name_list)
print(list(uper_case))

#length if string
string=["shanza","talhaaa","abdullah","ahmad"]
length_string=map(lambda str:len(str),string)
print(list(length_string))

#first character of each string...
str=["whanx","iaa","aghjkl","gh"]
first_chara=map(lambda f:f[0],str)
print(list(first_chara))

#filter function....
l1=[1,2,3,3,4,5,6,6,7,7,88,8,8,76,5,443,3,32,2,2,22]
even=filter(lambda x:x%2==0,l1)
print(list(even))

#str whoes length greater than 3
l1=["shanza","sha","tal","aha","ahmad","adb","dog","alii"]
length=filter(lambda x: len(x)>3,l1)
print(list(length))

#positive numbers.....
l2=[-4,8,9,8,3,2,4,-9,-6,-5,-3,-2]
posi=filter(lambda x:x>0,l2)
print(list(posi))

#reduce function....
from functools import reduce
l1=[1,2,3,43,4,5,5,6,6,7,78,6]
add=reduce(lambda x,y:x+y,l1)
print(add)

#multiply...
l1=[1,2,3,4,5,6,6,7,8,9]
multiply=reduce(lambda x,y:x*y,l1)
print(multiply)

#maximun
l1=[2,3,4,5,6,7,8,9]
maximun=reduce(lambda x,y:x if x>y else y,l1)
print(maximun)

#concatenated 
l1=["shanza","riaz","python","developer"]
concatenate=reduce(lambda x,y:x + " " + y,l1)
print(concatenate)
