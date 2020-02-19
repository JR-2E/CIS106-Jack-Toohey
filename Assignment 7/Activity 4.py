# This program calculates area of
# circles, rectangles, squares, and triangles.


def processCircle():
    print("What is the radius of the circle?")
    radius = float(input())
    circleArea = radius * radius * 3.14159
    print("The area of the circle is " + str(circleArea) + " square units.")

    return circleArea


def processRectangle():
    print("What is the base of the shape?")
    rectangleBase = float(input())
    print("What is the height of the shape?")
    rectangleHeight = float(input())
    rectangleArea = rectangleBase * rectangleHeight
    print("The area is " + str(rectangleArea) + " square units.")

    return rectangleArea


def processTriangle():
    print("Enter triangle base dimension.")
    triangleBase = float(input())
    print("Enter triangle height dimension.")
    triangleHeight = float(input())
    triangleArea = triangleBase * triangleHeight / 2
    print("The area of the triangle is " +
          str(triangleArea) + " square units.")

    return triangleArea

# Main
print("Which shape do you need to calculate the area of?
      A circle, triangle, square, rectangle, or rhombus?")
choice = input()
if choice == "circle" or choice == "Circle":
    processCircle()
else:
    if choice == "rectangle" or choice == "Rectangle" or
    choice == "square" or choice == "Square" or
    choice == "rhombus" or choice == "Rhombus":
        processRectangle()
    else:
        if choice == "triangle" or choice == "Triangle":
            processTriangle()
        else:
            print("No valid shape was entered.")
