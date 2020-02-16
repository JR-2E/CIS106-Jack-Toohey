# This program calculates weekly, monthly, and annual gross
# income from hourly wage, and average hours worked per week.


# get info from user
def get_hours():
    print("Enter your average weekly hours at work.")
    hours = float(input())
    return hours


def get_hourly_wage():
    print("Enter your hourly wage.")
    hourly_wage = float(input())
    return hourly_wage


# calculate income per various amounts of time
def calculate_weekly_income(hours, hourly_wage):
    weekly_income = hours * hourly_wage
    return weekly_income


def calculate_monthly_income(hours, hourly_wage):
    monthly_income = hours * hourly_wage * 52 / 12
    return monthly_income


def calculate_yearly_income(hours, hourly_wage):
    yearly_income = hours * hourly_wage * 52
    return yearly_income


# display results
def display_results(weekly_income, monthly_income, yearly_income):
    print("Your gross income is $" +
          str(weekly_income) + " per week, $" +
          str(monthly_income) + " per month, and $" +
          str(yearly_income) + " per year.")


def main():
    hours = get_hours()
    hourly_wage = get_hourly_wage()
    weekly_income = calculate_weekly_income(hours, hourly_wage)
    monthly_income = calculate_monthly_income(hours, hourly_wage)
    yearly_income = calculate_yearly_income(hours, hourly_wage)
    display_results(weekly_income, monthly_income, yearly_income)

main()
