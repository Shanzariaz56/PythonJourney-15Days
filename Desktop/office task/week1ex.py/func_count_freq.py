#specific character
s="shnza"
res=s.count("s")
print(res)

#make a function
def count_frequency(string):
    frequency={}
    for char in string:
        if char in frequency:
            frequency[char]+=1
        else:
            frequency[char]=1
    return frequency
string=input("enter the string::")
fre=count_frequency(string)
print(fre)

#by import counter form collection
from collections import Counter
def frequency(string):
    return Counter(string)

string = input("Enter the string: ")
res = frequency(string)
print(res)
