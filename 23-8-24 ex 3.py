def calculate_parking_charges(vehicle_type, hours):
    if vehicle_type == 'b':  # Bus/Truck
        charge_per_hour = 20
    elif vehicle_type == 'c':  # Car
        charge_per_hour = 10
    elif vehicle_type == 'm':  # Motorcycle/Bike
        charge_per_hour = 5
    elif vehicle_type == 'cy':  # Cycle
        charge_per_hour = 5
    else:
        return "Invalid vehicle type!"

    total_charges = charge_per_hour * hours
    return total_charges

def main():
    vehicle_type = input("Enter the type of vehicle (c for Car, b for Bus/Truck, m for Bike, cy for Cycle): ").lower()
    hours = int(input("Enter the number of hours parked: "))
    
    charges = calculate_parking_charges(vehicle_type, hours)
    
    if isinstance(charges, int):
        print(f"The total parking charges are: Rs. {charges}")
    else:
        print(charges)

if __name__ == "__main__":
    main()
