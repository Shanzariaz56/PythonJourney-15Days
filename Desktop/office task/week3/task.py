"""def task_task(user_list):
    try:
        # Convert the user input into a list of integers
        numbers = [int(x) for x in user_list]
    except ValueError:
        return "Invalid input, please enter valid numbers."

    # Initialize an empty list to store valid numbers
    valid_numbers = []

    # Process each number in the list
    for x in numbers:
        if 2000 <= x <= 4700:
            if x % 7 == 0 and x % 5 != 0:
                valid_numbers.append(x)

    # Convert list elements to strings and join with a comma
    if valid_numbers:
        result = ', '.join(map(str, valid_numbers))
        return f"Valid values within the range and meeting conditions: {result}"
    else:
        return "No values meet the criteria."

# Example usage
user_input = input("Enter a list of numbers separated by commas: ")
user_input_list = [x.strip() for x in user_input.split(',')]
print(task_task(user_input_list))"""
def integer_returner(num):
    if 2000 <= num <= 4700:
        if num % 5 != 0 and num % 7 == 0:
            list1.append(num)


list1 = []
n = 1
while n != 0:
    try:
        n = int(input("Enter an integer or enter 0 to exit: "))
    except ValueError as e:
        print("Please enter a valid integer.")
    else:
        if n != 0:
            integer_returner(n)


if list1:
    print("Numbers that satisfy the condition:", ", ".join(map(str, list1)))

else:
    print("No valid numbers were entered.")

