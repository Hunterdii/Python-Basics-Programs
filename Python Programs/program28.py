

def bitwise_and(a, b):
    return a & b

def bitwise_or(a, b):
    return a | b

def bitwise_xor(a, b):
    return a ^ b

def bitwise_not(a):
    return ~a

def bitwise_left_shift(a, b):
    return a << b

def bitwise_right_shift(a, b):
    return a >> b

# Get two integers from user
a = int(input("Enter an integer: "))
b = int(input("Enter another integer: "))

# Perform bitwise operations using user-defined functions
print("Bitwise AND:", bitwise_and(a, b))
print("Bitwise OR:", bitwise_or(a, b))
print("Bitwise XOR:", bitwise_xor(a, b))
print("Bitwise NOT (on first number):", bitwise_not(a))
print("Bitwise LEFT SHIFT (first number by second number):", bitwise_left_shift(a, b))
print("Bitwise RIGHT SHIFT (first number by second number):", bitwise_right_shift(a, b))
