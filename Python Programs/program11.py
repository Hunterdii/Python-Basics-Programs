
while True:
    print("\nChoose the operation to perform:")
    print("1. Addition of two numbers")
    print("2. Subtraction of two numbers")
    print("3. Multiplication of two numbers")
    print("4. Division of two numbers")
    print("5. Exit")
    
    choice = int(input("\nEnter your Choice: ")) 
    if choice == 1:
        print("\nAddition of two numbers")
        a = int(input("Enter the first number: "))
        b = int(input("Enter the second number: "))
        print("Addition = ",a+b)
        
    elif choice == 2:
        print("\nSubtraction of two numbers")
        a = int(input("Enter the first number: "))
        b = int(input("Enter the second number: "))
        print("Subtraction = ",a-b)
        
    elif choice == 3:
        print("\nMultiplication of two numbers")
        a = int(input("Enter the first number: "))
        b = int(input("Enter the second number: "))
        print("Multiplication = ",a*b)
        
    elif choice == 4:
        print("\nDivision of two numbers")
        a = int(input("Enter the first number: "))
        b = int(input("Enter the second number: "))
        print("Division =",a/b)

        print("Modulo Division = ",a%b)
    
    #exit condition to get out of the while loop
    elif choice == 5:
        print("Thank You! See you again.")
        break
    
    else:
        print("Invalid Input! Please, try again.")
