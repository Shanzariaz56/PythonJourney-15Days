#string....abs
s="shanzaaaaa"
print(s)
#string operation
#concatenation
s1="riaz"
s2=s+" "+s1
print(s2)
#string repetition
s3=s1*3
print(s3)
#string slicing...
print(s[0])
print(s[0:5])
print(s[6:])
#negative slicing
print(s[-1:])
print(s[-3:])
print(s[::-1])
#step slicing
print(s[1:6:2])
print(s[0:9:4])

#string function....
print(len(s))
print(s.count("a"))
print(s.upper())
print(s.lower())
print(s.endswith("yyyyy"))
print(s.find("a"))
print(s.capitalize())
print(s.replace("aaa","zzz"))

#string formating
# % operator
name="shanza"
age=20
string="my name is %s and my age is %d"%(name,age)
print(string)

# format method
string="my name is {} and my age is {}" .format(name,age)
print(string)

#f-string
print(f"my name is {name} and age is {age}")
#number formatting
pi=3.14667899
print(f"the amount we required after decimal will be: {pi:.2f}")