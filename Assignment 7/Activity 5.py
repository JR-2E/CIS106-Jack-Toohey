print("Enter your shoe size.")
shoeSize = float(input())
if shoeSize < 4:
    print("Your sock size is extra small.")
else:
    if shoeSize >= 4 and shoeSize <= 6:
        print("Your sock size is small.")
    else:
        if shoeSize >= 7 and shoeSize <= 9:
            print("Your sock size is medium.")
        else:
            if shoeSize >= 10 and shoeSize <= 12:
                print("Your sock size is large.")
            else:
                if shoeSize >= 13:
                    print("Your sock size is extra large.")
                else:
                    print("No valid shoe size was entered. Shoe size must be a positive number.")
