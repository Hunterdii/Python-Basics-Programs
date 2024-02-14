

def search_element(lst, element):
    if element in lst:
        return f"{element} found in the list"
    else:
        return f"{element} not found in the list"

def add_element(lst, element):
    lst.append(element)
    return f"{element} added to the list"

def update_element(lst, old_element, new_element):
    if old_element in lst:
        index = lst.index(old_element)
        lst[index] = new_element
        return f"{old_element} replaced with {new_element}"
    else:
        return f"{old_element} not found in the list"

def remove_element(lst, element):
    if element in lst:
        lst.remove(element)
        return f"{element} removed from the list"
    else:
        return f"{element} not found in the list"

def traverse_left_to_right(lst):
    print("Traversing left to right:")
    for element in lst:
        print(element)

def traverse_right_to_left(lst):
    print("Traversing right to left:")
    for element in reversed(lst):
        print(element)

# Get a list from user
lst = [int(x) for x in input("Enter a list of integers separated by space: ").split()]

# Perform operations on the list using user-defined functions
print(search_element(lst, 5))
print(add_element(lst, 10))
print(update_element(lst, 5, 15))
print(remove_element(lst, 20))
traverse_left_to_right(lst)
traverse_right_to_left(lst)
