n = int(input("Enter the number of terms: "))
a, b = 0, 1
if n <= 0:
   print("Please enter a positive integer")
elif n == 1:
   print("Fibonacci sequence upto", n, "term:")
   print(a)
else:
   print("Fibonacci sequence upto", n, "terms:")
   print(a)
   print(b)
   for i in range(2, n):
       c = a + b
       print(c)
       a, b = b, c
