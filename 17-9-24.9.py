case = int(input("Enter Case (1 for string, 2 for number): "))
val = input("Enter the value: ")
print("Palindrome" if val == val[::-1] else "Not Palindrome")
