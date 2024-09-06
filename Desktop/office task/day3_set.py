#set is a collection of non repetitive element
#it can take only unique 
s={1,2,2,3,3,4,5,6}
print(s)
s1={1,2,3,"shanza","riaz",(1,2,3,4,5),"shanza"}
print(s1)

#access and change element
s={1,2,3,3,4,"shanza","riaz",6}
print("shanza" in s)

#operation on set
s1={1,2,3,4,4,65,7,87,0,9}
print(s)
print(len(s))
print(s.remove(3))
print(s.pop())
print(s.union({1,88,55,333,99}))
s2={00,88,56,88,2,3,4,6}
print(s1.union(s2))
print(s1.intersection(s2))

#input from user
s=set()
for i in range(8):
    x=int(input("enter the number:"))
    s.add(x)
print(s)

#also using operator
a={1,2,3,3,4,54,5,6,77,9}
b={2,3,4,4,5,6,7,9,87,8,54}
print(a|b)
print(a&b)
print(a-b)
print(b-a)

#frozen set are those set that can never be change again once it being created
s1=frozenset({1,2,2,3,3})
print(s1)

#pop operation and set can be change at every excution
myset1 = {"Geeks", "for", 10, 52.7, True}
print(myset1)
myset1.pop()
print("Myset after removing :", myset1)
