# This program asks the user for distance in miles,
# and then converts it to yards, feet, and inches.


def get_miles():
    # get info from user
    print("Enter distance in miles.")
    miles = float(input())
    return miles


def calculate_yards(miles):
    # calculate distance in various units
    yards = miles * 1760
    return yards


def calculate_feet(miles):
    feet = miles * 5280
    return feet


def calculate_inches(miles):
    inches = miles * 63360
    return inches


def display_results(miles, yards, feet, inches):
    # Give the results to the user.
    print(str(miles) + " is " +
          str(yards) + " yards, " +
          str(feet) + " feet, and " +
          str(inches) + " inches.")


def main():
    miles = get_miles()
    yards = calculate_yards(miles)
    feet = calculate_feet(miles)
    inches = calculate_inches(miles)
    display_results(miles, yards, feet, inches)


main()
