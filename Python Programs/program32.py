n = int(input("Enter a number: "))
squares = []
cubes = []

for i in range(1, n+1):
    squares.append(i**2)
    cubes.append(i**3)

print("List of squares:", squares)
print("List of cubes:", cubes)
