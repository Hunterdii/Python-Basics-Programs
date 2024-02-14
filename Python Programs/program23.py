#function for addition of two numbers
def addition(a, b):
    sum = a + b
    print(a, "+", b, "=", sum)
    
#function for subtraction of two numbers
def subtraction(a, b):
    difference = a - b
    print(a, "-", b, "=", difference)
#function for multiplication of two numbers
def multiplication(a, b):
    product = a * b
    print(a, "*", b, "=", product)
    
#function for division of two numbers
def divide(a, b):
    quotient = a / b
    remainder = a % b
    print("Quotient of", a, "/", b, "=", quotient)
    print("Remainder of", a, "%", b, "=", remainder)

#Heading of menu-driven approach
print("WELCOME TO CALCULATOR")

#using the while loop to print menu list
while True:
    print("\nChoose the operation to perform:")
    print("1. Addition of two numbers")
    print("2. Subtraction of two numbers")
    print("3. Multiplication of two numbers")
    print("4. Division of two numbers")
    print("5. Exit")
    
    choice = int(input("\nEnter your Choice: "))
    
    #Calling the relevant method based on users choice using if-else 
    if choice == 1:
        print("\nAddition of two numbers")
        a = int(input("Enter the first number: "))
        b = int(input("Enter the second number: "))
        addition(a,b)
        
    elif choice == 2:
        print("\nSubtraction of two numbers")
        a = int(input("Enter the first number: "))
        b = int(input("Enter the second number: "))
        subtraction(a,b)
        
    elif choice == 3:
        print("\nMultiplication of two numbers")
        a = int(input("Enter the first number: "))
        b = int(input("Enter the second number: "))
        multiplication(a,b)
        
    elif choice == 4:
        print("\nDivision of two numbers")
        a = int(input("Enter the first number: "))
        b = int(input("Enter the second number: "))
        divide(a,b)
    
    #exit condition to get out of the while loop
    elif choice == 5:
        print("Thank You! See you again.")
        break
    
    else:
        print("Invalid Input! Please, try again.")
