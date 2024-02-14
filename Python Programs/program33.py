
my_tuple = ('apple', 'banana', 'orange', 'mango', 'grape', 'kiwi')
if 'banana' in my_tuple:
    print("Found 'banana' in the tuple.")
else:
    print("Could not find 'banana' in the tuple.")
print("Length of the tuple:", len(my_tuple))

# slicing the tuple
print("Sliced tuple (1st to 4th element):", my_tuple[0:4])
my_tuple = ('pear',) + my_tuple[1:-1] + ('watermelon',)
print("Modified tuple:", my_tuple)
index = int(input("Enter the index of the element to change (0 to 5): "))
element = input("Enter the new element: ")
my_tuple = my_tuple[:index] + (element,) + my_tuple[index+1:]
print("Modified tuple:", my_tuple)

