# normal fibnocci function
def fibonacci(num):
    fib=[]
    a,b=0,1
    while True:
        c=a+b
        if c>=num:
            break
        fib.append(c)
        a,b=b,c
    return fib
f=fibonacci(30)
for i in f:
    print(i)
    
    
# with generator function
def fibonacci(n):
    fib=[]
    a,b=0,1
    while True:
        c=a+b
        if c>=n:
            break
        yield c
        a,b=b,c
f=fibonacci(30)
while True:
    try:
        print(next(f))
    except StopIteration:
        break