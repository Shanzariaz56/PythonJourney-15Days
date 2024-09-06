def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
def modulus(a,b):
    return a%b
def calculator():
    while True:
        print("\nSelect operation:")
        print("1 - Addition")
        print("2 - Subtraction")
        print("3 - Multiplication")
        print("4 - Division")
        print("5 - Modulus")
        print("6 - Exit")
        
        choice = input("Enter your choice: ")

        if choice == '6':
            print("Exiting calculator. niklooo")
            break

        if choice in ['1', '2', '3', '4', '5']:
            a = int(input("Enter first number: "))
            b = int(input("Enter second number: "))
            
            if choice == '1':
                print("Result:", add(a, b))
            elif choice == '2':
                print("Result:", sub(a, b))
            elif choice == '3':
                print("Result:", mul(a, b))
            elif choice == '4':
                print("Result:", div(a, b))
            elif choice == '5':
                print("Result:", modulus(a, b))
        else:
            print("Invalid Input")
    
cal=calculator()
print(cal)
    