name="shahnaz"
age=20
height=5.8
a=True
print(name)
print(age)
print(height)
print(a)
print(type(a))
print(type(name))
print(type(height))
print(type(age))

#conditional statments.......
#conditional statement can be used to control flow of execution
n=int(input("enter the number"))
check="even" if n%2==0 else "odd"


#normal positive/negative
n=int(input("enter the number"))
if n>0:
    print("number is positive")
elif n<0:
    print("number is negative")
else:
    print("wrong")
    
#temperature
temp=int(input("entr the temperature:"))
if temp>40:
    print("its hot")
elif temp<20:
    print("its Cold")
else:
    print("temperature is normal")
    
#a program to print yes when the age entered by user is greater 18
age=int(input("enter the age"))
if age>18:
    print("yes")
else:
    print("no")
    
#e greatest of four numbers
a=int(input("enter the 1st number="))
b=int(input("enter the 2nd number="))
c=int(input("enter the 3rd number="))
d=int(input("enter the 4th number="))
if(a>b and a>c and a>d):
    print("1st number is Greater=",a)
elif(b>a and b>c and b>d):
    print("2nd number is Greater=",b)
elif(c>a and c>b and c>d):
    print("3rd number is Greater=",c)
else:
    print("4th number is greater=",d)

#another example...
n1=int(input("enter the 1st number="))
n2=int(input("enter the 1st number="))
n3=int(input("enter the 1st number="))
sum=n1+n2+n3
pec=(sum/300)*100
print(pec)
if n1>=33 and n2>=33 and n3>=33 and pec>=40:
    print("student has Passed")
elif n1<33 and n2<33 and n3<33:
    print("student failed")
else:
    print("failed due to overall percentage")
    
# program to detect these spams.
spam=["Make a lot of money", 'buy now', 'subscribe this', 'click this']
comment=input("enter the comment:")
comment_lower=comment.lower()
is_spam=any(keyword.lower() in comment_lower for keyword in spam)
if is_spam:
    print("comment is spam")
else:
    print("comment is not spam")

#n username contains less than 10 characters or not.  
name=input("enter your name")
length=len(name)
print(length)
if length<10:
    print("username can contain less than 10")
else:
    print("not less than one")

#calculate the grade of a student from his marks
n=int(input("enter the marks of student:"))
if (n>=90 and n<=100):
    Grade="Ex"
elif(n>=80 and n<=90):
    Grade="A"
elif(n>=70 and n<=80):
    Grade="B"
elif(n>=60 and n<=70):
    Grade="C"
elif(n>=50 and n<=60):
    Grade="D"
else:
    Grade="F"
print(Grade)
