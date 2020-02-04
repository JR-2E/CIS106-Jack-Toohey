# This program determines the amount of gallons that need to be
# bought to paint a room in the shape of a quadrilateral parallelagram.

# get needed info from user
print("What is the width of the room?")
room_width = float(input())
print("What is the height of the room?")
room_height = float(input())
print("What is the length of the room?")
room_length = float(input())
print("How many square feet will the gallon of paint cover?")
area_per_gallon = int(input())
print("How much does a gallon of paint cost?")
price_per_gallon = float(input())

# calc room wall area, gallons needed, and total cost of paint
total_room_area = 2 * room_length * room_height + 2 * room_width * room_height
total_gallons = total_room_area / area_per_gallon + 0.9999
total_cost = total_gallons * price_per_gallon

# give results to user
print("You will need " + str(total_gallons) +
      " gallons of paint " +
      " It will cost approximately $" + str(total_cost) + ".")
