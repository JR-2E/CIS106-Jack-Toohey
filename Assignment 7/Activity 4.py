def calcCircleArea(radius):
    circleArea = radius * radius * 3.14159    
    return circleArea

def calcRectangleArea(rectangleBase, rectangleHeight):
    rectangleArea = rectangleBase * rectangleHeight    
    return rectangleArea

def displayCircleArea(circleArea):
    print("The area of the circle is " + str(circleArea) + " square units.")

def displayRectangleArea(rectangleArea):
    print("The area of the rectangle is " + str(rectangleArea) + " square units.")

def getChoice():
    print("Enter rectangle to calculate the area of a rectangle, or circle to calculate the area of a circle.")
    choice = input()    
    return choice

def getRadius():
    print("What is the radius of the circle?")
    radius = float(input())    
    return radius

def getRectangleHeight():
    print("What is the height of the rectangle?")
    rectangleHeight = float(input())
    
    return rectangleHeight

def getRectangleBase():
    print("What is the base of the rectangle?")
    rectangleBase = float(input())    
    return rectangleBase

# Main
choice = getChoice()
if choice == "rectangle" or choice == "Rectangle":
    rectangleBase = getRectangleBase()
    rectangleHeight = getRectangleHeight()
    rectangleArea = calcRectangleArea(rectangleBase, rectangleHeight)
    displayRectangleArea(rectangleArea)
else:
    if choice == "circle" or choice == "Circle":
        radius = getRadius()
        circleArea = calcCircleArea(radius)
        displayCircleArea(circleArea)
    else:
        print("You must only enter either circle or rectangle.")
