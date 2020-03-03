# This program shows the column on a multiplication table for a certain number
print("What number would you like to see the column from a multiplication table for?")
number = int(input())
print("How far down the multiplication table should the column go?")
limit = int(input())
count = 1
while count <= limit:
    print(number * count)
    count = count + 1
