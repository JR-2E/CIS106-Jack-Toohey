# This program shows the column on a multiplication table for a certain number


def get_limit():
    print("How far down the multiplication table should the column go?")
    limit = int(input())
    return limit


def get_number():
    print("What number would you like to see the" +
          "column from a multiplication table for?")
    number = int(input())
    return number


def loop(count, number, limit):
    count = 1
    while count <= limit:
        print(number * count)
        count = count + 1

# Main
count = 1
number = get_number()
limit = get_limit()
loop(count, number, limit)
