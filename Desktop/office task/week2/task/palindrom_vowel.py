def palindrom(string):
    new_string=string
    vowels=["a","e","i","o","u"]
    is_palindrom=False
    if string==string[::-1]:
        is_palindrom=True
        for i in string:
            if i in vowels:
                new_string=new_string.replace(i,"")
        print(new_string)
                   
    else:
        is_palindrom=False
    print(is_palindrom)
    
s=input("enter the string:")
if s=="" and string==" ":
    print("not a palindrom:")
else:
    res=palindrom(s)
    print(res)