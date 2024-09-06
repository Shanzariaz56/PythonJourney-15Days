#with set.....
l1=[1,2,3,3,4,4,5,5]
l2=[2,3,344,5,6,6,7,9]
l3=l1+l2
print(l3)
remove_dup=list(set(l3))
print(remove_dup)
#without set..,
l1=[1,2,3,4,4,66,7,8,6,7,5,9]
l2=[4,5,6,6,7,8,9,1,3,2]
merge=l1+l2
new_uni=[]
for i in merge:
    if i not in new_uni:
        new_uni.append(i)
        
new_uni.sort()
print(new_uni)
