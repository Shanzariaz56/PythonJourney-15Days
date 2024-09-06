# raise exception error...
def div(x,y):
    if y==0:
        raise ValueError("not divisble by zero")
    return x/y
try:
    x=int(input("enter the number 1::"))
    y=int(input("enter the number 2::"))
    res=div(a,b)
    print(res)
except ValueError as err:
    print(err)
