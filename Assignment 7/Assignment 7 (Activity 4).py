# This program calculates the area of circles, and rectangles.


def get_choice():
    print("Enter rectangle to calculate the area of a rectangle," +
          " or circle to calculate the area of a circle.")
    choice = input()
    return choice


# First comes the circle functions
def get_radius():
    print("Enter the radius of the circle.")
    radius = float(input())
    return radius


def calc_circle_area(radius):
    circle_area = radius * radius * 3.14159
    return circle_area


def display_circle_area(circle_area):
    print("The area of the circle is " +
          str(circle_area))


# Now for rectangle functions
def get_rectangle_base():
    print("What is the base of the rectangle?")
    rectangle_base = float(input())
    return rectangle_base


def get_rectangle_height():
    print("What is the height of the rectangle?")
    rectangle_height = float(input())
    return rectangle_height


def calc_rectangle_area(rectangle_base, rectangle_height):
    rectangle_area = rectangle_base * rectangle_height
    return rectangle_area


def display_rectangle_area(rectangle_area):
    print("The area of the rectangle is " +
          str(rectangle_area))


def main():
    choice = get_choice()
    if choice == "circle" or choice == "Circle":
        radius = get_radius()
        circle_area = calc_circle_area(radius)
        circle_area = display_circle_area(circle_area)
    elif choice == "rectangle" or choice == "Rectangle":
        rectangle_base = get_rectangle_base()
        rectangle_height = get_rectangle_height()
        rectangle_area = calc_rectangle_area(rectangle_base, rectangle_height)
        display_rectangle_area(rectangle_area)
    else:
        print("You must only enter either circle or rectangle.")


main()
