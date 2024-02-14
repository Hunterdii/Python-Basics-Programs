n = int(input("Enter the value of n: "))

# Generate the dictionary
my_dict = {}
for x in range(1, n+1):
    my_dict[x] = x*x

# Print the dictionary
print(my_dict)
