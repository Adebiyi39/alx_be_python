from datetime import datetime, timedelta

# Part 1: Display the current date and time
def display_current_datetime():
    current_date = datetime.now()
    print("Current Date and Time:", current_date.strftime("%Y-%m-%d %H:%M:%S"))
    return current_date


# Part 2: Calculate a future date
def calculate_future_date(current_date):
    days = int(input("Enter number of days to add: "))
    future_date = current_date + timedelta(days=days)
    print("Future Date:", future_date.strftime("%Y-%m-%d"))


# Main program
if __name__ == "__main__":
    current_date = display_current_datetime()
    calculate_future_date(current_date)
