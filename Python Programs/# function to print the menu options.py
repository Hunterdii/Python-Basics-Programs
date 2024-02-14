# function to print the menu options
def print_menu():
    print("1. Create an empty dictionary")
    print("2. Add a key-value pair")
    print("3. Remove a key-value pair")
    print("4. Access a value for a given key")
    print("5. Check if a key exists in the dictionary")
    print("6. Update the value for a given key")
    print("7. Print all the keys")
    print("8. Print all the values")
    print("9. Print all the key-value pairs")
    print("10. Clear the dictionary")
    print("11. Exit the program")

# create an empty dictionary
my_dict = {}

# loop until the user chooses to exit
while True:
    # print the menu
    print_menu()

    # get the user's choice
    choice = int(input("Enter your choice (1-11): "))

    # execute the selected option
    if choice == 1:
        my_dict = {}

    elif choice == 2:
        key = input("Enter the key: ")
        value = input("Enter the value: ")
        my_dict[key] = value

    elif choice == 3:
        key = input("Enter the key to remove: ")
        if key in my_dict:
            del my_dict[key]
            print("Key-value pair removed")
        else:
            print("Key not found")

    elif choice == 4:
        key = input("Enter the key to access: ")
        if key in my_dict:
            print("Value: ", my_dict[key])
        else:
            print("Key not found")

    elif choice == 5:
        key = input("Enter the key to check: ")
        if key in my_dict:
            print("Key found")
        else:
            print("Key not found")

    elif choice == 6:
        key = input("Enter the key to update: ")
        if key in my_dict:
            value = input("Enter the new value: ")
            my_dict[key] = value
            print("Value updated")
        else:
            print("Key not found")

    elif choice == 7:
        print("Keys: ", list(my_dict.keys()))

    elif choice == 8:
        print("Values: ", list(my_dict.values()))

    elif choice == 9:
        print("Key-value pairs: ", list(my_dict.items()))

    elif choice == 10:
        my_dict.clear()
        print("Dictionary cleared")

    elif choice == 11:
        print("Exiting program...")
        break

    else:
        print("Invalid choice. Please enter a number from 1-11.")
