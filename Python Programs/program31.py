words = ['apple', 'banana', 'orange', 'egg', 'igloo', 'umbrella']
vowels = ['a', 'e', 'i', 'o', 'u']
new_words = []

for word in words:
    if word[0].lower() in vowels:
        new_words.append(word.upper())
    else:
        new_words.append(word)

print(new_words)
