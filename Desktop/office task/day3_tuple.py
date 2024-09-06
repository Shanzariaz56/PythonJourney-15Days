#tuple is immutable and can never be change once it can be created
#when we need fixed data that can never be change
t1=(1,2,3,4,5,6,7,8,9)
print(t1)

#create an empty tuple...
empty_tuple=tuple()
print(empty_tuple)

#convert string into tuple....
str="shanza"
t2=tuple(str)
print(t2)

#tuple indexing/slicing.....
t1=(1,2,3,4,3,5,6,7,7,8,88,9)
print(t1[0])
print(t1[2:7])
print(t1[-1:])
print(t1[::2]) # step by step
print(t1[::-1])

t1=(1,2,3,4,5)
t1=(10,20,8,9)
print(t1)

#concatenating tuple
t1=(1,2,3,4)
t2=(5,6,7,8)
t3=t1+t2
print(t3)

#packing and unpacking a tuple
packed_tuple=1,2,3
print(packed_tuple)

#unpack....
t1=(1,2,3)
a,b,c=t1
print(a)
print(b)
print(c)

#repeating tuple
t1=(1,2,3)
t2=t1*4
print(t2)

#method of tuples
t1=(1,2,3,3,5,6,8,9)
print(t1[::-1]) #reverse tuple
sorted_tuple=tuple(sorted(t1))  #sorted tuple
print(sorted_tuple) 
#traverse a tuple
t1=(1,2,3,4,5,6,7)
for i in t1:
    print(i)
#count specific no...
t1=(1,2,3,4,5,5,6,6,76,7,7,7)
print(t1.count(7))

#delete a tuple
t1=(1,2,3,4,5,6,7)
del t1
print(t1)
t1=(1,2,3,4,5,6,7,7,9)
print(max(t1))
print(min(t1))
print(sum(t1))
print(len(t1))

#find the tuple,that contain given element from list of tuple
l1=[(11,22),(1,2),(11,87),(98,11),(11,87),(1,7)]
x=11
output=[]
for i in l1:
    if x in i:
        output.append(i)
print(output)

#sawp tuple elements
t1=(1,2,3,3)
t2=(4,5,6,7)
t3=t1
t1=t2
t2=t3
print(t1)
print(t2)

#chk element existence
t1=(1,2,3,4)
x=int(input("enter the number:"))
if x in t1:
    print(x)
