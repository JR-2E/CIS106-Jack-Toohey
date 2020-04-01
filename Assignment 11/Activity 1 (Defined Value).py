def getYear():
    print("What year do you want to know the "+
          "amount of days in each month for?")
    given_year = int(input())
    return given_year


def display_results(leap_year, leap_year_array, normal_year_array):
    count = 0
    if leap_year is True:
        for count in range(0, 11 + 1, 1):
            print(normal_year_array[count])
    else:
        for count in range(0, 11 + 1, 1):
            print(leap_year_array[count])


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


def display_results(leap_year, leap_year_array, normal_year_array):
    count = 0
    if leap_year is True:
        for count in range(0, 11 + 1, 1):
            print(normal_year_array[count])
    else:
        for count in range(0, 11 + 1, 1):
            print(leap_year_array[count])


def main():
    leap_year_array = [""] * (12)
    normal_year_array = [""] * (12)

    normal_year_array[0] = "January = 31 days"
    normal_year_array[1] = "February = 28 days"
    normal_year_array[2] = "March = 31 days"
    normal_year_array[3] = "April = 30 days"
    normal_year_array[4] = "May = 31 days"
    normal_year_array[5] = "June = 30 days"
    normal_year_array[6] = "July = 31 days"
    normal_year_array[7] = "August = 31 days"
    normal_year_array[8] = "September = 30 days"
    normal_year_array[9] = "October = 31 days"
    normal_year_array[10] = "November = 30 days"
    normal_year_array[11] = "December = 31 days"
    leap_year_array[0] = "January = 31 days"
    leap_year_array[1] = "February = 29 days"
    leap_year_array[2] = "March = 31 days"
    leap_year_array[3] = "April = 30 days"
    leap_year_array[4] = "May = 31 days"
    leap_year_array[5] = "June = 30 days"
    leap_year_array[6] = "July = 31 days"
    leap_year_array[7] = "August = 31 days"
    leap_year_array[8] = "September = 30 days"
    leap_year_array[9] = "October = 31 days"
    leap_year_array[10] = "November = 30 days"
    leap_year_array[11] = "December = 31 days"
    year = getYear()
    leap_year = get_leap_year(year)
    display_results(leap_year, normal_year_array, leap_year_array)

main()
