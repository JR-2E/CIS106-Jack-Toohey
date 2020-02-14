# This program takes length and width in feet,
# and converts it to area in square yards

def get_length():
    print("Enter room length.")
    length = float(input())
    return length

def get_width():
    print("Enter room width.")
    width = float(input())
    return width

def calculate_area(length, width):
    area = length * width / 9
    return area


def display_result(area):
    print("The room has an area of " + str(area) + " square yards.")


def main():
    length = get_length()
    width = get_width()
    area = calculate_area(length, width)
    display_result(area)


main()
