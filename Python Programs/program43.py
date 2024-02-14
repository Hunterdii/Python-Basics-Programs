# Personal information
name = input("Enter Name:\n")
birth_date = input("Date of birth:\n")
email = input("Email:\n")
address = input("Address:\n")
contact = input("Contact:\n")

# Write the information to a file
with open("personal_info.txt", "w") as f:
    f.write(f"Name: {name}\n")
    f.write(f"Birth Date: {birth_date}\n")
    f.write(f"Email: {email}\n")
    f.write(f"Address: {address}\n")
    f.write(f"Contact: {contact}\n")

# Read and print the information from the file
with open("personal_info.txt", "r") as f:
    lines = f.readlines()

print("Personal Information:")
print("---------------------")
for line in lines:
    print(line.strip())
