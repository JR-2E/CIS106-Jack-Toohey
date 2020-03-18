def getLimit():
    print("How far down the multiplication table should the column go?")
    limit = int(input())
    
    return limit

def getNumber():
    print("What number would you like to see the column from a multiplication table for?")
    number = int(input())
    
    return number

def loop(limit, number):
    count = 1
    for count in range(1, limit + 1, 1):
        print(str(number) + "*" + str(count) + "=" + str(number * count))

# Main
number = getNumber()
limit = getLimit()
loop(limit, number)
