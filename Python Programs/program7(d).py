number1=int(input("Enter Number1"))
number2=int(input("Enter Number2"))
print("Before swapping number1={0}\t number2={1}".format(number1,number2))
number1=number1^number2
number2=number1^number2
number1=number1^number2
print("After swapping number1={0}\t number2={1}".format(number1,number2))
