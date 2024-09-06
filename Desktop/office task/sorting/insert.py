#Insert sort is like a playcard in which you consider that the first element as sorted
def insertsort(arr):
    n=len(arr)
    for i in range(1,n):
        key=arr[i]
        j=i-1
        while j>=0 and key<arr[j]:
            arr[j+1]=arr[j]
            j=j-1
        arr[j+1]=key
arr=[9,5,1,4,3]
insertsort(arr)
print("insertion sorting::",arr)
