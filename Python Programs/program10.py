print("Choose 1. Triangle \n 2. circle\n 3. Rectangle \n 4. square \n 5. Cylinder")
option=int(input("Enter Your Option:"))
if option ==1:
    base=int(input("Enter base of Triangle:"))
    height=int(input("Enter height of Triangle:"))
    print("The Area of Triangle is =",0.5*base*height)
elif option==2:
    radius=int(input("Enter the radius of Circle:"))
    print("The Area of circle is =",3.14159*(radius**2))
elif option ==3:
    length=int(input("Enter the length of Rectangle:"))
    breadth=int(input("Enter the breadth of Rectangle:"))
    print("The Area of Rectangle is =",length*breadth)
elif option ==4:
    length=int(input("Enter the length of Square:"))
    print("The Area of the Square is=",length**2)
elif option==5:
    radius=int(input("Enter the radius of the Cylinder:"))
    print("The Area of Cylinder is =",2*(3.14159)*(radius**2))
else:
    print("Choose the Correct Option")
