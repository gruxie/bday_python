import datetime
import math

def get_next_birthday(birthday, today):
    """
    Calculate the next birthday date based on the current date.
    Handles leap years, especially for birthdays on February 29th.
    """
    year = today.year
    try:
        next_birthday = birthday.replace(year=year)
    except ValueError:
        # This handles February 29 on non-leap years by setting to February 28
        next_birthday = birthday.replace(year=year, month=2, day=28)
    
    if next_birthday < today:
        try:
            next_birthday = birthday.replace(year=year + 1)
        except ValueError:
            # Handle February 29 on non-leap years
            next_birthday = birthday.replace(year=year + 1, month=2, day=28)
    
    return next_birthday

def calculate_days_until_birthday(birthday_str):
    """
    Calculate the number of days until the next birthday.
    Rounds up to the nearest whole day if there's a fractional part.
    """
    # Define the expected input format
    input_format = "%m%d%Y"
    
    try:
        # Parse the input string into a datetime object
        birthday = datetime.datetime.strptime(birthday_str, input_format)
    except ValueError:
        print("Invalid format. Please enter your birthday in mmddyyyy format.")
        return
    
    today = datetime.datetime.now()
    next_birthday = get_next_birthday(birthday, today)
    
    # Calculate the difference
    delta = next_birthday - today
    days_until = delta.total_seconds() / 86400  # Convert seconds to days
    
    # If the birthday is today, days_until will be very small (close to 0)
    if days_until <= 0:
        days_until = 0
    
    # Round up to the nearest whole day
    days_until_rounded = math.ceil(days_until)
    
    print(f"Days until your next birthday: {days_until_rounded}")

def main():
    birthday_input = input("Enter your birthday (mmddyyyy): ")
    calculate_days_until_birthday(birthday_input)

if __name__ == "__main__":
    main()
