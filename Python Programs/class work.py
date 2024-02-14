def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def sum_of_n(n):
    return sum(range(1,n+1))

def is_prime(n):
    if n < 2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i == 0:
            return False
    return True

while True:
    print("Menu:")
    print("1. Find the factorial of a number")
    print("2. Find the sum of n integers")
    print("3. The number is prime or not")
    print("4. EXIT")
    choice = int(input("Enter your choice (1-4): "))
    if choice == 1:
        n = int(input("Enter a number: "))
        print("Factorial of",n,"is",factorial(n))
    elif choice == 2:
        n = int(input("Enter a number: "))
        print("Sum of first",n,"integers is",sum_of_n(n))
    elif choice == 3:
        n = int(input("Enter a number: "))
        if is_prime(n):
            print(n,"is a prime number")
        else:
            print(n,"is not a prime number")
    elif choice == 4:
        break
    else:
        print("Invalid choice. Enter a number between 1 and 4.")
