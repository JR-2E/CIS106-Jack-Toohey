# This program asks the user how old they are in years,
# then converts the years into months, days, hours, and seconds.

# asking the user their age
print("How old are you? (In years)")
years = int(input())

# calculations from input
months = years * 12
days = years * 365
hours = years * 8766
seconds = years * 31557600

# showing user age in different measurements
print("You are approxiately " +
      str(months) + " months, " +
      str(days) + " days, " +
      str(hours) + " hours, and " + 
      str(seconds) + " seconds old.")
