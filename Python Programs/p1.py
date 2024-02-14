def countB(word):
    print(word) 
    count=0
    for b in word:
      if(b=='b'):
        count+=1
    return count
print("Number of 'b'= ", countB ("abbbabbaaa"))