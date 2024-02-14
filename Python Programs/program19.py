num = int(input("number: "))
sum = 0
n = len(str(num))
temp = num
while temp > 0:
   digit = temp % 10
   sum += digit ** n
   temp //= 10
if num == sum:
   print(num, "is an Armstrong number")
else:
   print(num, "is not an Armstrong number")
