my_list = [1, 2, 3, 2, 4, 5, 3, 6, 7, 6, 8, 9, 9, 1]

# create an empty list to store unique elements
unique_list = []

# loop through each element in the original list
for element in my_list:
    # check if the element is not already in the unique list
    if element not in unique_list:
        # add the element to the unique list
        unique_list.append(element)

# print the unique list
print("Original list:", my_list)
print("Unique list:", unique_list)
