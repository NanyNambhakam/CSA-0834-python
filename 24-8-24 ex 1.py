def reverse_word(word):
    reversed_word = ""
    for char in word:
        reversed_word = char + reversed_word
    return reversed_word

input_word = "Hello"
output_word = reverse_word(input_word)
print("Original Word:", input_word)
print("Reversed Word:", output_word)
