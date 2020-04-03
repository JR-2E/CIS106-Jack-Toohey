# Comments go here...


def get_year():
    print("What year do you want to know the " +
          "amount of days in each month for?")
    given_year = int(input())
    return given_year


def get_leap_year(given_year):
    if given_year % 400 == 0:
        return True

    if given_year % 100 == 0:
        return False

    if given_year % 4 == 0:
        return True

    return False


def get_month():
    print("Enter the month number of the month " +
            "which you want the number of days.")
    month_number = int(input())
    return month_number


def display_results(month_name, month_days):
        print(f"{month_name} has {month_days} days")


def get_month_name(month):
    months = ["January", "February", "March", "April",
        "May", "June", "July", "August", "September", 
        "October", "November", "December"]

    if month < 1 or month > 12:
        return "Unknown"
    return months[month - 1]


def get_month_days(year, month):
    if get_leap_year(year):
        days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    else:
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if month < 1 or month > 12:
        return "Unknown"
    return days[month - 1]



def main():
    while True:
        year = get_year()
        month = get_month()
        if month < 1 or month > 12:
            break
        month_name = get_month_name(month)
        month_days = get_month_days(year, month)
        display_results(month_name, month_days)


main()
