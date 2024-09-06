# here are the error handling
# try can be excute the block of code
# except can contain the excepted error
# finaly can excute that your c0de is finally excute

def divide():
    try:
        x=int(input("enter the number 1::"))
        y=int(input("enter the number 2::"))
        res=x//y
        print("result after division::",res)
    except ZeroDivisionError:
        print("sorry! yoy are divided by 00")
    except ValueError:
        print("sorry! you may enter special character")
print(divide())    

# another example:
def calculation():
    try:
        x=int(input("enter the number 1::"))
        y=int(input("enter the number 2::"))
        res=x//y
    except ZeroDivisionError:
        print("sorry! yoy are divided by 00")
    except ValueError:
        print("sorry! you may enter special character")
    except Exception as err:
        print(err)
    else:
        print("result after division::",res) 
        
calculation()
    