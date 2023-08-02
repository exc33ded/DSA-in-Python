# Define a function to count the frequency of words in a given list of words.

words = ['apple', 'orange', 'banana', 'apple', 'orange', 'apple'] 

def count_word_frequency(words):
    words_count = {}
    for word in words:
        words_count[word] = words_count.get(word, 0) + 1
    return words_count

print(count_word_frequency(words))