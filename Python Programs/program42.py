from collections import Counter

d1 = {'a':100, 'b':200, 'c':300}
d2 = {'a':300, 'b':200, 'd':400}

# Use Counter to merge the dictionaries and add the values for common keys
merged_dict = Counter(d1) + Counter(d2)

# Print the merged dictionary
print(merged_dict)
