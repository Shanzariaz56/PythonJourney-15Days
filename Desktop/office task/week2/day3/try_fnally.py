# try finally (finally must be executed)
def div():
    try:
        x=int(input("enter the number 1::"))
        y=int(input("enter the number 2::"))
        res=x//y
        print("result:",res)
    finally:
        print("you are succesfulll!!!!!!!!!!!!!")
        
div()

# another
def temp_convert(var):
   try:
      return int(var)
   except ValueError as Argument:
      print("The argument does not contain numbers\n",Argument)
temp_convert("xyz")

        