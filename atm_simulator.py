
balance = 10000
transactions = []

while True:
    print("\nWelcome to the bank")
    print("1. Check balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    print("5. Check history")

    choice = int(input("Enter your choice: "))

    if choice < 1 or choice > 5:
        print("Invalid choice selection")

    elif choice == 1:
        print(f"Your balance is ₹{balance}")

    elif choice == 2:
        amount = int(input("How much are you going to deposit? "))

        if amount > 0:
            balance = balance + amount
            transactions.append(f"Deposited ₹{amount}")
            print(f"Your new balance is ₹{balance}")
        else:
            print("Enter a valid amount")

    elif choice == 3:
        amount = int(input("How much do you want to withdraw? "))

        if amount > 0 and amount <= balance:
            balance = balance - amount
            transactions.append(f"Withdrew ₹{amount}")
            print("Withdrawal successful!")
            print(f"Your current balance is ₹{balance}")
        else:
            print("Invalid amount or insufficient balance")

    elif choice == 4:
        print("Thank you for visiting. Please visit again!")
        break

    elif choice == 5:
        if len(transactions) == 0:
            print("No transactions yet")
        else:
            print("Transaction History:")
            for transaction in transactions:
                print(transaction)
