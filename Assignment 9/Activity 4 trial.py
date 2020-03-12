def calcCircleArea(radius):
    circleArea = radius * radius * 3.14159
    return circleArea


def calcRectangleArea(rectangleBase, rectangleHeight):
    rectangleArea = rectangleBase * rectangleHeight
    return rectangleArea


def displayCircleArea(circleArea):
    print("The area of the circle is " + str(circleArea) + " square units.")


def displayRectangleArea(rectangleArea):
    print("The area of the rectangle is " +
          str(rectangleArea) + " square units.")


def getAmount():
    print("How many shapes would you like to calculate the area of?")
    amount = int(input())
    return amount


def getChoice():
    print("Enter rectangle to calculate the area of a rectangle," +
          "or circle to calculate the area of a circle.")
    choice = input()
    return choice


def getRadius():
    print("What is the radius of the circle?")
    radius = float(input())
    return radius


def getRectangleBase():
    print("What is the base of the rectangle?")
    rectangleBase = float(input())
    return rectangleBase


def getRectangleHeight():
    print("What is the height of the rectangle?")
    rectangleHeight = float(input())
    return rectangleHeight


def loop(amount):
    getChoice()
    if choice == "rectangle" or choice == "Rectangle":
        getRectangleBase()
        getRectangleHeight()
        calcRectangleArea(rectangleBase, rectangleHeight)
        displayRectangleArea(rectangleArea)
    else:
        if choice == "circle" or choice == "Circle":
            getRadius()
            calcCircleArea(radius)
            displayCircleArea(circleArea)
        else:
            print("You must only enter either circle or rectangle.")
    count = 1
    while count <= amount - 1:
        getChoice()
        if choice == "rectangle" or choice == "Rectangle":
            getRectangleBase()
            getRectangleHeight()
            calcRectangleArea(rectangleBase, rectangleHeight)
            displayRectangleArea(rectangleArea)
        else:
            if choice == "circle" or choice == "Circle":
                getRadius()
                calcCircleArea(radius)
                displayCircleArea(circleArea)
            else:
                print("You must only enter either circle or rectangle.")
        count = count + 1
    return area

# Main
amount = getAmount()
loop(amount)
