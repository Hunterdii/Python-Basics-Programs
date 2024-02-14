
def convert_to_list(sentence):
    word_list = sentence.split()
    return word_list

def find_word_position(word, word_list):
    if word in word_list:
        index = word_list.index(word)
        return f"{word} found at position {index+1}"
    else:
        return f"{word} not found in the list"

# Get a sentence from user
sentence = input("Enter a sentence: ")

# Convert the sentence into a list of words using the convert_to_list function
word_list = convert_to_list(sentence)

# Get a word from the user to search in the list
word = input("Enter a word to search in the list: ")

# Find the position of the word in the list using the find_word_position function
print(find_word_position(word, word_list))
