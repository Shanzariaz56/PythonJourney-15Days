# simple divide decorator
# that is cutomize decorators
def div(a,b):
    return a/b
def divide(func):
    def inner_div(a,b):
        if a<b:
            a,b=b,a
        return func(a,b)
    return inner_div
d=divide(div)
print(d(2,4))

# another example
def ice_land(func):
   # def inner():
        print("Welcome! to iceland")
        func()
   # return inner
@ice_land
def ice():
    print("Which one icecream you want")
#ice()   