# This program converts width/length in feet
# to area in square yards

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

def calculate_area():
    global area
    area = length * width / 9
    return area

def display_results():
    print("The area of the room is", area, "square yards")

def main():
    get_length()
    get_width()
    calculate_area()
    display_results()


main()
