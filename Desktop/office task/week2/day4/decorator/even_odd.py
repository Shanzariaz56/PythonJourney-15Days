def even_num(func):
    def inner(num):
        if num%2==0:
            print("EVEN")
        else:
            print("ODD")
        func(num)
    return inner

@even_num
def even(x):
    print("the number will be:",x)
even(4)
    