def calculate_total_balance():
    total_balance = 0

    for i in range(1, 5):
        denomination = int(input(f"Enter the {i}th Denomination: "))
        number_of_notes = int(input(f"Enter the {i}th Denomination number of notes: "))
        total_balance += denomination * number_of_notes

    print(f"Total Available Balance in ATM: {total_balance}")
calculate_total_balance()
