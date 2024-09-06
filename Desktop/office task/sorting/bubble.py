#bubble sort
def bubble(arr):
    n=len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if arr[j]>arr[j+1]:
                temp=arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=temp
    return arr
arr=[1,3,4,5,6,9,6,4,3,2,2,4]
res=bubble(arr)
print(res)

#by using swapped
def bubble(arr):
    n=len(arr)
    for i in range(n):
        swapped =False
        for j in range(n-i-1):
              if arr[j]>arr[j+1]:
                temp=arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=temp
                swapped=True
        if not swapped:
            break
arr=[1,3,4,5,6,9,6,4,3,2,2,4]
bubble(arr)

print('Sorted Array:')
print(arr)