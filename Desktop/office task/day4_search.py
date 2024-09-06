#linear search is used when we need a sequential search 
#binary search is used o=for sorted array
#binary search can work on divide and conquer approach and linear search work on sequential approach
arr=[1,2,2,3,3,4,5,7,6,3,78,8,90,0]
index=-1
x=int(input("enter the number::"))
for i in range(len(arr)):
    if(arr[i]==x):
        index=i
if(index==-1):
    print("not found::")
else:
    print("element found::",index)
    
    
arr=[1,2,2,3,3,4,5,7,6,3,78,8,90,0]
x=int(input("enter the number::"))
for i in range(len(arr)):
    if arr[i]==x:
        print("element found:")
        break
else:
    print("elment not found:")   
    
# with function 
def linear_search(arr,hit):
    for i in range(len(arr)):
        if(arr[i]==hit):
            return i
        else:
            return -1
arr=[12,3,3,4,4,5,5,6,6,7,7,8,8,9]
hit=int(input("enter the number:"))
target=linear_search(arr,hit)
if target!=-1:
    print(f"element found at index{target}") 
    
#binary search....
def binary_search(arr,target):
    left,right=0,len(arr)-1
    while left<=right:
        mid=(left+right)//2
        if arr[mid]==target:
            return mid
        elif arr[mid]<target:
            left=mid+1
        else:
            right=mid-1
    return -1
arr=[2,3,4,5,6,7,8,9,10]
target=int(input("enter the number::"))
res=binary_search(arr,target)
if res!=-1:
    print(f"elment found at index: {res}")   
else:
    print("not found") 
    
#through unsorted array
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:

        mid = (high + low) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1


arr = [5, 43, 7, 8, 3, 2, 5, 31, 34, 66, 9]
arr_sorted=sorted(arr)
print(arr_sorted)
target = int(input("Enter the target number: "))
target_index = binary_search(arr_sorted, target)

if target_index != -1:
    print(f"The target {target} is present at index : {target_index}")
        