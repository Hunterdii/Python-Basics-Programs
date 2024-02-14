# Open the file in read mode
file = open("TEXT.txt", "r")

# Use seek() to set the position of the file pointer
file.seek(10)

# Use tell() to get the current position of the file pointer
print("Current position of file pointer:", file.tell())

# Use tail() to get the remaining content of the file
content = file.read()
print("Content from current position:", content)
 
# Close the file
file.close()
