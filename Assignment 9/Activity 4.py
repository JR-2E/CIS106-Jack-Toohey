# This program asks the user how many shapes need their area calculated,
# then calculates the area and displays it to the user.


def calc_circle_area(radius):
    circle_area = radius * radius * 3.14159
    return circle_area


def calc_rectangle_area(rectangle_base, rectangle_height):
    rectangle_area = rectangle_base * rectangle_height
    return rectangle_area


def display_circle_area(circle_area):
    print("The area of the circle is " + str(circle_area) + " square units.")


def display_rectangle_area(rectangle_area):
    print("The area of the rectangle is " +
          str(rectangle_area) +
          " square units.")


def get_amount():
    print("How many shapes would you like to calculate the area of?")
    amount = int(input())
    return amount


def get_choice():
    print("Enter rectangle to calculate the area of a rectangle," +
          "or circle to calculate the area of a circle.")
    choice = input()
    return choice


def get_radius():
    print("What is the radius of the circle?")
    radius = float(input())
    return radius


def getrectangle_base():
    print("What is the base of the rectangle?")
    rectangle_base = float(input())
    return rectangle_base


def getrectangle_height():
    print("What is the height of the rectangle?")
    rectangle_height = float(input())
    return rectangle_height


def loop(amount):
    count = 0
    while count < amount:
        choice = get_choice()
        if choice == "rectangle" or choice == "Rectangle":
            rectangle_base = getrectangle_base()
            rectangle_height = getrectangle_height()
            rectangle_area = calc_rectangle_area(rectangle_base, rectangle_height)
            display_rectangle_area(rectangle_area)
        else:
            if choice == "circle" or choice == "Circle":
                radius = get_radius()
                circle_area = calc_circle_area(radius)
                display_circle_area(circle_area)
            else:
                print("You must only enter either circle or rectangle.")
        count = count + 1


# Main
amount = get_amount()
loop(amount)
