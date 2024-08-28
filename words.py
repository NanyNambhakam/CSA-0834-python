def count_words(input_string):
    words = input_string.split()
    return len(words)
text = "Hello, how are you doing today?"
word_count = count_words(text)
print(f"The number of words in the string is: {word_count}")
