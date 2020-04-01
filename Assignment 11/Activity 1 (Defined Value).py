def get_year():
    print("What year do you want to know the " +
          "amount of days in each month for?")
    given_year = int(input())
    return given_year


def get_leap_year(given_year):
    year = given_year
    while year >= 4:
        if year == 4:
            leap_year = True
        else:
            leap_year = False
        year = year - 4
    year = given_year
    while year >= 100:
        if year == 100:
            leap_year = False
        year = year - 100
    year = given_year
    while year >= 400:
        if year == 400:
            leap_year = True
        year = year - 400
    return leap_year


def display_results(leap_year, normal_year_day_array, normal_year_month_array,
                    leap_year_day_array, leap_year_month_array):
    if leap_year is True:
        print("Enter the month number of the month " +
              "which you want the number of days.")
        month_number = int(input())
        print(leap_year_month_array[month_number - 1])
        print(leap_year_day_array[month_number - 1])
    else:
        print("Enter the month number of the month " +
              "which you want the number of days.")
        month_number = int(input())
        print(normal_year_month_array[month_number - 1])
        print(normal_year_day_array[month_number - 1])


def main():
    normal_year_day_array = [""] * (12)
    normal_year_month_array = [""] * (12)
    leap_year_day_array = [""] * (12)
    leap_year_month_array = [""] * (12)

    leap_year_day_array = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    leap_year_month_array = ["January", "February", "March", "April",
                             "May", "June", "July", "August", "September", "October", "November", "December"]
    normal_year_day_array = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    normal_year_month_array = ["January", "February", "March", "April",
                             "May", "June", "July", "August", "September", "October", "November", "December"]
    year = get_year()
    leap_year = get_leap_year(year)
    display_results(leap_year, normal_year_day_array, normal_year_month_array,
                    leap_year_day_array, leap_year_month_array)

main()
