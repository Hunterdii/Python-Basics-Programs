n = int(input("Enter the range: "))

# Create the dictionary
binary_dict = {}
for i in range(1, n+1):
    binary_dict[i] = bin(i)[2:].zfill(len(bin(n)[2:]))

# Print the dictionary
for key, value in binary_dict.items():
    print(key, ": ", value)

