
def print_dict(my_dict):
    """Utility function to print the contents of a dictionary"""
    print("\nDictionary contents:")
    for key, value in my_dict.items():
        print(f"{key}: {value}")

# Initialize an empty dictionary
my_dict = {}

# Start the menu loop
while True:
    print("\nDictionary Operations:")
    print("1. Add key-value pair")
    print("2. Remove key-value pair")
    print("3. Update value of a key")
    print("4. Check if key exists")
    print("5. Get value of a key")
    print("6. Get all keys")
    print("7. Get all values")
    print("8. Print dictionary")
    print("9. Exit")

    # Get user's choice
    choice = int(input("\nEnter your choice (1-9): "))

    # Perform the corresponding operation
    if choice == 1:
        key = input("Enter key: ")
        value = input("Enter value: ")
        my_dict[key] = value
        print_dict(my_dict)

    elif choice == 2:
        key = input("Enter key to remove: ")
        if key in my_dict:
            del my_dict[key]
            print_dict(my_dict)
        else:
            print(f"Key '{key}' not found!")

    elif choice == 3:
        key = input("Enter key to update: ")
        if key in my_dict:
            value = input("Enter new value: ")
            my_dict[key] = value
            print_dict(my_dict)
        else:
            print(f"Key '{key}' not found!")

    elif choice == 4:
        key = input("Enter key to check: ")
        if key in my_dict:
            print(f"Key '{key}' found!")
        else:
            print(f"Key '{key}' not found!")

    elif choice == 5:
        key = input("Enter key to get value: ")
        if key in my_dict:
            value = my_dict[key]
            print(f"Value of '{key}' is '{value}'")
        else:
            print(f"Key '{key}' not found!")

    elif choice == 6:
        keys = list(my_dict.keys())
        print(f"All keys: {keys}")

    elif choice == 7:
        values = list(my_dict.values())
        print(f"All values: {values}")

    elif choice == 8:
        print_dict(my_dict)

    elif choice == 9:
        print("Exiting...")
        break

    else:
        print("Invalid choice! Try again.")
