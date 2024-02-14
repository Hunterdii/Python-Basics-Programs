lower = int(input("Enter the lower limit of the interval: "))
upper = int(input("Enter the upper limit of the interval: "))

# iterate through each number in the interval
for num in range(lower, upper + 1):
   # initialize sum and number of digits
   sum = 0
   n = len(str(num))

   # calculate the sum of the cube of each digit
   temp = num
   while temp > 0:
      digit = temp % 10
      sum += digit ** n
      temp //= 10

   # check if the number is an Armstrong number
   if num == sum:
      print(num)

