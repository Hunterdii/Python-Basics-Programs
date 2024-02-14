num_set = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
num_set.add(11)
num_set.update([12, 13, 14])
print("Set after adding elements:", num_set)
num_set.remove(11)
num_set.discard(12)
print("Set after removing elements:", num_set)
popped_element = num_set.pop()
print("Set after popping an element:", num_set)
print("Popped element:", popped_element)
num_set.clear()
print("Set after clearing all elements:", num_set)

