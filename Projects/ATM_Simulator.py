def check_balance(balance):
    print("current balance:", balance)
    
def deposite(balance):
    amount = int(input("Enter deposite Amount:"))
    
    if amount > 0:
        balance = balance + amount
        print("Amount deposited successfully")
        
    else:
        print("invalid amount")    
    return balance
def withdrawal(balance):
    amount =int(input("Enter withdrawal amount:"))
    
    if amount <= 0:
        print("invalid amount")
    elif amount <= balance:
        balance = balance-amount
        print("withdrawal successfully")
    else:
        print("insuficient balance")
         
    return balance
balance =10000
PIN ="2424"    
attempts =0
logged_in = False

while attempts < 3:
    PIN=input("Enter your ATM PIN:")
    if PIN == PIN:
        logged_in = True
        break
    else:
        attempts = attempts + 1
        print("incorrect PIN:")
        
if logged_in:
    while True:
        print("\n ---ATM MENU---")        
        print("1.check balance")
        print("2.deposite money")
        print("3.withdraw money")
        print("4.Exit")
        choice = input("Enter your choice:")
         
        if choice == "1":
            check_balance(balance)
        elif choice == "2":
            balance = deposite(balance)
        elif choice == "3":
            balance =withdrawal(balance)
        elif choice == "4":
            print("Thank you for using ATM!")
            break
        else:
            print("invalid choice")
    else:
        print("Your account is lokced ")        
         
     