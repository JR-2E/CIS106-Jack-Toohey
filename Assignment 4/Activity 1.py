# This program calculates weekly, monthly, and annual gross
# income from hourly wage, and average hours worked per week.

# collect needed info from user
print("How many hours of work do you average per week?")
avg_hours_per_week = float(input())
print("How much money (USD) do you make per hour?")
hourly_wage = float(input())

# calculate income per various amounts of time
weekly_income = avg_hours_per_week * hourly_wage
yearly_income = weekly_income * 52
monthly_income = yearly_income / 12

# give results to user
print("Your gross income is $" +
      str(weekly_income) + " per week, $" +
      str(monthly_income) + " per month, and $" +
      str(yearly_income) + " per year.")
