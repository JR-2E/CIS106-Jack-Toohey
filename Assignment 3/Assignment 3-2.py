# This program converts the length and width of a room (in feet) to the area of the room in square yards.
print("Enter length of room ")
lengthOfRoom = float(input())
print("Enter width of room ")
widthOfRoom = float(input())
squareYardsOfRoom = lengthOfRoom * widthOfRoom / 9
print("Area of room is " + str(squareYardsOfRoom) + " square yards.")
