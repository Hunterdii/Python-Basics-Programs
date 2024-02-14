# take input from the user
num = int(input("Enter a positive integer: "))

# initialize variables
sum = 0
i = 1

# calculate the sum of natural numbers using while loop
while i <= num:
    sum += i
    i += 1

# print the sum of natural numbers
print("The sum of first", num, "natural numbers is", sum)
