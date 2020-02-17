# This program asks the user for distance in miles,
# and then converts it to yards, feet, and inches.


# get info from user
def get_miles():
    print("Enter distance in miles.")
    miles = float(input())
    return miles


# calculate distance in various units
def calculate_yards(miles):
    yards = miles * 1760
    return yards


def calculate_feet(miles):
    feet = miles * 5280
    return feet


def calculate_inches(miles):
    inches = miles * 63360
    return inches


# Give the results to the user.
def display_results(miles, yards, feet, inches):
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
