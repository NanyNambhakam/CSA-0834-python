def count_letter_occurrence(string, letter):
    return string.count(letter)
input_string = "Hello, how are you doing today?"
letter_to_count = "o"
occurrences = count_letter_occurrence(input_string, letter_to_count)
print(f"The letter '{letter_to_count}' occurs {occurrences} times in the string.")
