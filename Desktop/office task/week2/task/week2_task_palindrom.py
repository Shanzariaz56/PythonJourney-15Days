# take a string and check that string is palindrom
def palindrom(string):
    if string==string[::-1]:
        print("that is the palindrom string:",string)
    else:
        print("not a palindrom string",string)

s=input("enter the string::")
if s=="" or " " in s:
    print("not a palindrom its just can empty")
else:    
    res=palindrom(s) 
    print(res)