class BankAccount:
    def __init__(self):
        self.balance= 0
        
    def deposit(self,amount):
        if amount>0:
            self.balance+=amount
            print("your ammount is successfully Deposit:",self.balance)
        else:
            print("Try Again")
    def withdrawal(self,amount):
        if amount <= 0:
            print("Enter a valid amount")
        elif amount > balance:
            print("You may have Insufficient balance")
        elif amount>=balance:
            print(f"you may successfully withdraw {amount}")
            self.balance-=amount
        else:
            print("Try Again you may press incorrect keyword")
    def balance_chk(self):
        print(f"your remaining balance is {self.balance}") 
   
obj=BankAccount()
while True:
        print("\nSelect Option:")
        print("1 - Deposit")
        print("2 - Withdrawal")
        print("3 - Balance check")
        print("4 - Exit")
        
        choice = input("Enter your choice: ")
        
        if choice=="4":
            print("nikloooooo")
            
        if choice in ['1', '2', '3']:
            if choice=="1":
                obj.deposit(int(input("Enter Amount you want to Deposit::")))
            elif choice=="2":
                obj.withdrawal(int(input("Enter Amount you want to withdrawal::")))
            elif choice=="3":
                obj.balance_chk()
                
                