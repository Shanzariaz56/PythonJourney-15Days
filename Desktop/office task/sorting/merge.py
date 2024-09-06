#merge sort........
def merge_sort(arr):
    if len(arr)<=1:
        return arr
    mid=len(arr)//2
    l_half=arr[:mid]
    r_half=arr[mid:]
    l_half=merge_sort(l_half)
    r_half=merge_sort(r_half)
    return merge(l_half,r_half)
def merge(left,right):
    new=[]
    i=j=0 
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            new.append(left[i])
            i+=1
        else:
            new.append(right[j])
            j+=1
    new.extend(left[i:])
    new.extend(right[j:])
    return new
arr=[2,5,6,9,7,5,3,66,77,98,34,22]
sorted_arr=merge_sort(arr)
print(sorted_arr)   
