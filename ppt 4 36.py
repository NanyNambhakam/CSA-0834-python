num1 = int(input("Enter first number: "))

num2 = int(input("Enter second number: "))

divi = 0

try:
    divi = int(num1/num2)

except ZeroDivisionError:
    print("enter the second number above zero")

print("Division is : ",divi)
