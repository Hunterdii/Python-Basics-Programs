my_tuple = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37,)
prime_list = []
for num in my_tuple:
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
        
            prime_list.append(num)

print("Prime numbers from the tuple:", prime_list)
