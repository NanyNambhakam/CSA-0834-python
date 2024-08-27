def calculate_pow(x, n):
    return x ** n

def calculate_add(x, n):
    return x + n

def calculate_sub(x, n):
    return x - n

def calculate_mul(x, n):
    return x * n

def calculate_div(x, n):
    if n != 0:
        return x / n
    else:
        return "Error: Division by zero is not allowed."

def main():
    print("Welcome to the Python Calculator!")
    x = float(input("Enter the first number (x): "))
    n = float(input("Enter the second number (n): "))
    
    print("\nChoose the operation you want to perform:")
    print("1. Power (x^n)")
    print("2. Addition (x+n)")
    print("3. Subtraction (x-n)")
    print("4. Multiplication (x*n)")
    print("5. Division (x/n)")
    
    choice = input("Enter the number corresponding to your choice (1-5): ")
    
    if choice == '1':
        result = calculate_pow(x, n)
        operation = "Power"
    elif choice == '2':
        result = calculate_add(x, n)
        operation = "Addition"
    elif choice == '3':
        result = calculate_sub(x, n)
        operation = "Subtraction"
    elif choice == '4':
        result = calculate_mul(x, n)
        operation = "Multiplication"
    elif choice == '5':
        result = calculate_div(x, n)
        operation = "Division"
    else:
        result = "Invalid choice. Please select a number between 1 and 5."
        operation = "None"
    
    print(f"\nResult of {operation}: {result}")

if __name__ == "__main__":
    main()
