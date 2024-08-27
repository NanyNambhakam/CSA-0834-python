def is_leap_year(year):
    """Check if a year is a leap year."""
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def get_anniversary_date(date_str):
    """Determine the anniversary date based on whether the year is a leap year."""
    day, month, year = map(int, date_str.split('/'))
    
    if is_leap_year(year):
        next_anniversary = year + 1
        print(f"Given Anniversary Year: Leap Year. Anniversary Date: {day:02d}/{month:02d}/{next_anniversary}")
    else:
        previous_anniversary = year - 1
        print(f"Given Anniversary Year: Non Leap Year. Anniversary Date: {day:02d}/{month:02d}/{previous_anniversary}")

input_date = input("Enter Date (DD/MM/YYYY): ")
get_anniversary_date(input_date)
