x = int(input("Enter X: "))
n = int(input("Enter N: "))
choice = int(input("Choose operation: 1.Pow 2.Add 3.Sub 4.Mul 5.Div: "))

if choice == 1:
    print(f"Pow(X,N) = {x ** n}")
elif choice == 2:
    print(f"Add(X,N) = {x + n}")
elif choice == 3:
    print(f"Sub(X,N) = {x - n}")
elif choice == 4:
    print(f"Mul(X,N) = {x * n}")
elif choice == 5:
    print(f"Div(X,N) = {x / n if n != 0 else 'undefined (division by zero)'}")
else:
    print("Invalid choice")
