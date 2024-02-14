1number=int(input("To check prime or not:\n"))
flag = False

if number == 1:
    print(number, "is not a prime number")
elif number > 1:
    for i in range(2, number):
        if (number % i) == 0:
            flag = True
            break
    if flag:
        print(number, "is not a prime number")
    else:
        print(number, "is a prime number")
