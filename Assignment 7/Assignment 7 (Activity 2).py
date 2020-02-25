# This program calculates age from years into
# months, days, hours, and seconds


# get info from user
def get_years():
    print("Enter your age, in years.")
    years = float(input())
    return years


# calculate age in different units
def calculate_months(years):
    months = years * 12
    return months


def calculate_days(years):
    days = years * 365
    return days


def calculate_hours(years):
    hours = years * 8766
    return hours


def calculate_seconds(years):
    seconds = years * 31557600
    return seconds


# display results
def display_results(years, months, days, hours, seconds):
    print("You are approxiately " +
          str(months) + " months, " +
          str(days) + " days, " +
          str(hours) + " hours, and " +
          str(seconds) + " seconds old.")


def main():
    years = get_years()
    months = calculate_months(years)
    days = calculate_days(years)
    hours = calculate_hours(years)
    seconds = calculate_seconds(years)
    display_results(years, months, days, hours, seconds)


main()
