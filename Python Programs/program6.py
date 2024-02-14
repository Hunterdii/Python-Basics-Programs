import cmath
a = int(input("Enter a value:\n"))
b = int(input("Enter b value:\n"))
c = int(input("Enter c value:\n"))
d = (b**2) - (4*a*c)
sol1 = (-b-cmath.sqrt(d))/(2*a)
sol2 = (-b+cmath.sqrt(d))/(2*a)
print('The solutions are {0} and {1}'.format(sol1,sol2))
