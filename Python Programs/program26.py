
def display_menu():
    print("1. Concatenate two strings")
    print("2. Repeat a string")
    print("3. Slice a string")
    print("4. Exit")
while True:
    display_menu()
    choice = input("Enter your choice (1-4): ")
    if choice == "1":
        str1 = input("Enter first string: ")
        str2 = input("Enter second string: ")
        result = str1 + str2
        print("The concatenated string is:", result)
    elif choice == "2":
        str1 = input("Enter a string: ")
        n = int(input("Enter the number of times to repeat: "))
        result = str1 * n
        print("The repeated string is:", result)
    elif choice == "3":
        str1 = input("Enter a string: ")
        start = int(input("Enter the starting index: "))
        end = int(input("Enter the ending index: "))
        result = str1[start:end]
        print("The sliced string is:", result)
    elif choice == "4":
        print("Exiting the program...")
        break
    else:
        print("Invalid input. Please enter a valid choice.")
