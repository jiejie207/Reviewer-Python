balance = 1000

def check_balance():
    print("Balance:", balance)

def deposit():
    global balance
    amount = int(input("Enter amount: "))
    balance += amount
    print("Deposit successful!")

def withdraw():
    global balance
    amount = int(input("Enter amount: "))

    if amount <= balance:
        balance -= amount
        print("Withdrawal successful!")
    else:
        print("Not enough balance!")


while True:
    print("\n=== ATM ===")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = input("Choose: ")

    if choice == "1":
        check_balance()

    elif choice == "2":
        deposit()

    elif choice == "3":
        withdraw()

    elif choice == "4":
        print("Thank you!")
        break

    else:
        print("Invalid choice!")