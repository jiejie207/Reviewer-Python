names = []

def add_name():
    name = input("Enter a name:")
    names.append(name)



while True:
    print("1. Add a name")
    print("2. Show names")
    print("3. Exit")

    choice = input("Enter your choice:")

    if choice == "1":
        add_name()
    elif choice == "2":
        print(names)
    elif choice == "3":
        break
    else:
        print("Invalid choice. Please try again.")

