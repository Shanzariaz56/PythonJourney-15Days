#loop can be used to iterate the block of code but in a sequence
#for loop is basically more helpful in iterating list,tuple,dict,string,range 
#while loop is used for alos block of code but mostly used for specific condition


#sum of list number:
l1=[1,2,4,6,8,9,4,3,2]
sum=0
for i in l1:
    sum=sum+i
print(sum)

response=""
while response!="yes":
    response=input("Do you want to continue? (yes/no): ")

#sending email to multiple receipent
recipients=["shanza@gamil.com","ali@gamil.com","talha@gamil.com","hamza@gamil.com"]
for i in recipients:
    print(f"sending email to {i}")
    
#calculate the average temperature
temp=[45.8, 67.0 ,89.90,43.5,34.0]
sum=0
for i in temp:
    sum=sum+i
avg=sum/len(temp)
print("the average of temperature will be:",avg)

#print table of 5...
n=int(input("enter the number:"))
for i in range(1,11):
    print(n,"*",i,"=",n*i)

#print 1 to 50 using a while loop
i=1
while(i<=50):
    print(i)
    i=i+1 
    
list=[1,2,3,4,"shanza",4.0]
i=0
while i<len(list):
    print(list[i])
    i=i+1

#for loop using different range
l=[1,2,3,4,5,7,8,9,9]
for i in range(2,7,2):
    print(i)
    
#for loop with break
for i  in range(0,30):
    print(i)
    if i==10:
        break
#check a prime number r not
num=int(input("enter the number:"))
is_prime=True
if num<=1:
    is_prime=False
else:
    for i in range(2,num):
        if(num%2==0):
            is_prime=False
            break
if is_prime:
    print(f"that is the prime number {num}")
else:
    print(f"not a prime numner {num}")
    
#calculate the factorial of number
n=int(input("enter the number:"))
fac=1
for i in range(1,n+1):
    fac=fac*i 
print(fac) 

#for star sequence...
n=int(input("enter the number of lines:"))
for i in range(n):
    print(" "*(n-i-1),end="")
    print("*"*(2*i+1))

n=int(input("enter the number of lines:"))
for i in range(n):
    print("*"*(1*i+1))
    
n=int(input("enter the number of lines:"))
for i in range(n):
    if i==0 or i==(n-1):
        print("*"*n)
    else:
        print("*"+" "*(2*(n-3)+1)+"*")
        
n=int(input("enter the number:"))
for i in range(10,1,-1):
    print(n,"*",i,"=",n*i)
    
a="shanza"
print(repr(a))