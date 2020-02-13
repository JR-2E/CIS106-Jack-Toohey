# This program determines the amount of gallons that need to be bought,
# when painting a room in the shape of a quadrilateral parallelagram.


# get needed info from user
def get_length():
        global length
        print("What is the length of the room, in feet?")
        length = float(input())
        return length

def get_width():
        global width
        print("What is the width of the room, in feet?")
        width = float(input())
        return width

def get_height():
        global height
        print("What is the height of the room, in feet?")
        height = float(input())
        return height

def get_cost():
        global cost
        print("What is the cost of the paint per gallon?")
        cost = float(input())
        return cost

def get_paint_coverage():
        global coverage
        print("How much area, in square feet, does a gallon of paint cover?")
        coverage = float(input())
        return coverage

# calculate room wall area, gallons needed, and total cost
def calculate_area_of_walls():
        global area
        area = length * width * 9
        return area

def calculate_gallons():
        global gallons
        gallons = area / coverage
        return gallons

def calculate_total_cost():
        global total_cost
        total_cost = gallons * cost
        return total_cost

def display_results():
        global display_results
        print("You will need " + str(int(gallons)) +
        " gallons of paint " +
        " It will cost approximately $" + str(total_cost) + ".")
        return display_results


def main():
        get_length()
        get_width()
        get_height()
        get_cost()
        get_paint_coverage()
        calculate_area_of_walls()
        calculate_gallons()
        calculate_total_cost()
        display_results()

main()
