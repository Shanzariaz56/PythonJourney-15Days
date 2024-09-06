""""import random

counter = 0
sum_even = 0
random_numbers = []
max1 = 0
max2 = 0

for i in range(100):
    current_number = random.randint(1, 100)
    random_numbers.append(current_number)

    if current_number % 2 == 0:
        sum_even += current_number
        counter += 1

    if current_number > max1:
        max2 = max1
        max1 = current_number
    elif current_number > max2:
        max2 = current_number

average = sum_even / counter

print("Random numbers list: ", random_numbers)
print("Average of even numbers:", average)
print("Total even numbers:", counter)
print("Second Largest:", max2)"""

def bubble(arr):
    n=len(arr)-1
    for i in range(n):
        if arr[i]>arr[i+1]:
            arr[i],arr[i+1]=arr[i+1],arr[i]
    return arr
            
cars = [5, 3, 8, 4, 2]
sorted=bubble(cars)
print(sorted)