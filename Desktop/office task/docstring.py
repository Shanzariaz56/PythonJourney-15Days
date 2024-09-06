# docstring ,means you may add documentation in your code
# here that is the func that calculate the arithmetic operation
def calculation():
    """here is the function name :calculation 
    then perfrom calculation"""

    a=int(input("enter the number1:"))
    b=int(input("enter the number2:"))
    
    """ the first can take the first value from the user
    and second can take second value from the user
    and then print the arithmetic operation"""
    
    print("Addition:",a+b)
    print("subtraction:",a-b)
    print("multiplication:",a*b)
    print("division:",a/b)
    
""" now here call the function 
create a variable and call function"""
print(calculation.__doc__)
