#in selection sort first i can first take the minimum number and then iterate the whole array
#select on the base of minimun element
def selectionsort(arr):
    n=len(arr)
    for i in range(n):
        mini=i
        for j in range(i+1,n):
            if arr[j]<arr[mini]:
                mini=j
        (arr[i], arr[mini]) = (arr[mini], arr[i])

arr=[2,3,4,8,9,5,4,3,2,1,0]
selectionsort(arr)
print("sorted array through selection search::",arr)

#inner loop is just iterate over the array
#exact swapping work can be done by outter loop
def selectionsort(arr):
    n=len(arr)
    for i in range(n):
        min=i
        for j in range(i+1,n):
            if arr[j]<arr[min]:
                min=j
            if min!=i:
                temp=arr[min]
                arr[min]=arr[i]
                arr[i]=temp
arr=[2,3,4,8,9,5,4,3,2,1,0]
selectionsort(arr)
print("sorted array through selection search::",arr)
            

