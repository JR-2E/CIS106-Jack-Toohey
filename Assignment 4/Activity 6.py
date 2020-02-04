# This program determines the amount of gallons that need to be
# bought to paint a room in the shape of a quadrilateral parallelagram.

# get needed info from user
print("What is the width of the room?")
roomWidth = float(input())
print("What is the height of the room?")
roomHeight = float(input())
print("What is the length of the room?")
roomLength = float(input())
print("How many square feet will the gallon of paint cover?")
areaPerGallon = int(input())
print("How much does a gallon of paint cost?")
pricePerGallon = float(input())

# calc room wall area, gallons needed, and total cost of paint
totalRoomArea = 2 * roomLength * roomHeight + 2 * roomWidth * roomHeight
totalGallons = totalRoomArea / areaPerGallon + 0.9999
totalCost = totalGallons * pricePerGallon

# give results to user
print("You will need " + str(totalGallons) +
      " gallons of paint " +
      " It will cost approximately $" + str(totalCost) + ".")
