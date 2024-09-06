#list........
l1=[1,2,3,4,5,6,79,6,8,0,8]
#indexing and slicing
print(l1[0])
print(l1[0:7])
#method of list....
print(l1.sort())
print(l1)
print(l1.append("shanza"))
print(l1)
print(l1.reverse())
print(l1)
print(l1.pop(2))
print(l1.insert(3,"shanza"))
print(l1)
print(l1.remove("shanza"))
print(l1)
print(l1.extend([7,8]))
print(l1)
#reverse list without function
l1=[1,2,3,4,5]
print(l1[::-1])
#list comprehension
l1=[x for x in range(10)]
print(l1)

#square of list
square=[x**2 for x in range(20)]
print(square)

#even
even=[x for x in range(20) if x%2==0]
print(even)

#grid...
grid=[(x,y) for x in range(4) for y in range(7)]
print(grid)

#odd number
odd=[x for x in range(3) if x%2!=0]
print(odd)
l1=[1,2,3,4,5]
l2=[3,4,5,6]
l3=l1+l2
print(l3)
l1=["shnza","riaz","talha"]
uper_case=[i.upper() for i in l1]
print(uper_case)

lists=[[1,2,3],[1234,556],[7,8,9,94]]
sample=[items for sublist in lists for items in sublist]
print(sample)


