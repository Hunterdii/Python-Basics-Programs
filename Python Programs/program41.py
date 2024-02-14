dictionary={}
string=input("Enter String :\n").lower()

for i in range(97,123):
   dictionary[chr(i)]=string.count(chr(i))
print(dictionary)
