lower_value = int(input("Enter Lower value:\n"))
upper_value = int(input("Enter Upper value:\n"))

print("Prime numbers between", lower_value, "and", upper_value, "are:")

for num in range(lower_value, upper_value + 1):
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)
