def calculate_tax(income):
    if income < 150000:
        tax = 0
    elif 150001 <= income <= 300000:
        tax = income * 0.10
    elif 300001 <= income <= 500000:
        tax = income * 0.20
    else:
        tax = income * 0.30
    return tax

if __name__ == "__main__":
    income = float(input("Enter your taxable income: ₹"))
    tax = calculate_tax(income)
    print(f"The tax on an income of ₹{income} is: ₹{tax:.2f}")
