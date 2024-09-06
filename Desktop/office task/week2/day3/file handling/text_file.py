# open a file
"""try:
    file=open("shanzy.txt","r")
    content=file.read()
    print(content)
finally:
    file.close()"""
    
# also can be open like that 
with open("shanzy.txt","r") as file:
    f=file.read()
    print(f)
# write in file when we can open file in write mode it can rewrite the already existing file
with open("shanzy.txt","w") as file:
    f=file.write("shanzyyyy")
    print(f)
    
    