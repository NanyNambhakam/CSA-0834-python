try:
    age = float(input("Enter your age: "))
    if age >= 18:
        print("You are eligible to vote.")
    elif age >= 0:
        print(f"You are allowed to vote after {18 - int(age)} years.")
    else:
        print("Invalid input. Please enter a valid age.")
except ValueError:
    print("Invalid input. Please enter a numerical value.")
