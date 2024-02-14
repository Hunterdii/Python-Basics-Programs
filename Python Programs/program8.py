number = float(input("Enter a number: "))
if number > 0:
   print("Positive number")
   if number%2==0:
     print("Even Number")
   else:
     print("Odd Number")

elif number == 0:
   print("Zero")
else:
   print("Negative number")
