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

    leap_year_day_array[0] = "31 days"
    leap_year_day_array[1] = "29 days"
    leap_year_day_array[2] = "31 days"
    leap_year_day_array[3] = "30 days"
    leap_year_day_array[4] = "31 days"
    leap_year_day_array[5] = "30 days"
    leap_year_day_array[6] = "31 days"
    leap_year_day_array[7] = "31 days"
    leap_year_day_array[8] = "30 days"
    leap_year_day_array[9] = "31 days"
    leap_year_day_array[10] = "30 days"
    leap_year_day_array[11] = "31 days"
    leap_year_month_array[0] = "January"
    leap_year_month_array[1] = "February"
    leap_year_month_array[2] = "March"
    leap_year_month_array[3] = "April"
    leap_year_month_array[4] = "May"
    leap_year_month_array[5] = "June"
    leap_year_month_array[6] = "July"
    leap_year_month_array[7] = "August"
    leap_year_month_array[8] = "September"
    leap_year_month_array[9] = "October"
    leap_year_month_array[10] = "November"
    leap_year_month_array[11] = "December"

    normal_year_day_array[0] = "31 days"
    normal_year_day_array[1] = "28 days"
    normal_year_day_array[2] = "31 days"
    normal_year_day_array[3] = "0 days"
    normal_year_day_array[4] = "31 days"
    normal_year_day_array[5] = "30 days"
    normal_year_day_array[6] = "31 days"
    normal_year_day_array[7] = "31 days"
    normal_year_day_array[8] = "30 days"
    normal_year_day_array[9] = "31 days"
    normal_year_day_array[10] = "30 days"
    normal_year_day_array[11] = "31 days"
    normal_year_month_array[0] = "January"
    normal_year_month_array[1] = "February"
    normal_year_month_array[2] = "March"
    normal_year_month_array[3] = "April"
    normal_year_month_array[4] = "May"
    normal_year_month_array[5] = "June"
    normal_year_month_array[6] = "July"
    normal_year_month_array[7] = "August"
    normal_year_month_array[8] = "September"
    normal_year_month_array[9] = "October"
    normal_year_month_array[10] = "November"
    normal_year_month_array[11] = "December"

    year = get_year()
    leap_year = get_leap_year(year)
    display_results(leap_year, normal_year_day_array, normal_year_month_array,
                    leap_year_day_array, leap_year_month_array)

main()
