n=int(input("Enter a number"))

try:
    if(n==0):
        print("Zero")
    elif(n>0):
            print("Positive")
    else:
                raise ValueError
except ValueError:
                print("Value Error Enter positive numbers")
