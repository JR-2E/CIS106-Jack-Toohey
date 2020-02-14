# This program takes the length, width, and height
# of a room, and the coverage/cost of a gallon of paint,
# and converts it to gallons needed and cost of paint.

def get_length():
    print("Enter room length.")
    length = float(input())
    return length

def get_width():
    print("Enter room width.")
    width = float(input())
    return width

def get_height():
    print("Enter room height.")
    height = float(input())
    return height

def get_cost():
    print("Enter the cost of one gallon of paint.")
    cost = float(input())
    return cost

def get_coverage():
    print("Enter how many feet one gallon of paint covers.")
    coverage = float(input())
    return coverage

def calculate_area(length,height,width):
    area = 2 * length * height + 2 * width * height
    return area

def calculate_gallons(area,coverage):
    gallons = area / coverage + 0.9999
    return gallons

def calculate_total_cost(gallons,cost):
    total_cost = gallons * cost
    return total_cost

def display_result(gallons,total_cost):
    print("You will need " + str(int(gallons)) + " gallons of paint. It will cost $" + str(total_cost) + ".")


def main():
    length = get_length()
    width = get_width()
    height = get_height()
    cost = get_cost()
    coverage = get_coverage()
    area = calculate_area(length,height,width)
    gallons = calculate_gallons(area,coverage)
    total_cost = calculate_total_cost(gallons,cost)
    display_result(gallons,total_cost)

main()
