# This program calculates weekly, monthly, and annual gross
# income from hourly wage, and average hours worked per week.

# collect needed info from user
print("How many hours of work do you average per week?")
avgHoursPerWeek = float(input())
print("How much money (USD) do you make per hour?")
hourlyWage = float(input())

# calculate income per various amounts of time
weeklyIncome = avgHoursPerWeek * hourlyWage
yearlyIncome = weeklyIncome * 52
monthlyIncome = yearlyIncome / 12

# give results to user
print("Your gross income is $" +
      str(weeklyIncome) + " per week, $" +
      str(monthlyIncome) + " per month, and $" +
      str(yearlyIncome) + " per year.")
