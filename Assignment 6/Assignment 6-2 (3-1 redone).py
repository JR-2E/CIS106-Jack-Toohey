# This program takes length and width in feet,
# and converts it to area in square yards

#get weight of hydropgen in grams
def get_grams():
    print("Enter grams of hydrogen.")
    grams = float(input())
    return grams

# calculate the moles of hydrogen in given weight
def calculate_moles(grams):
    moles = grams / 1.0079
    return moles

# give user the number of moles in given weight
def display_result(grams, moles):
    print(str(grams) + " Grams of Hydrogen is " +
          str(moles) + " moles of Hydrogen")


def main():
    grams = get_grams()
    moles = calculate_moles(grams)
    display_result(grams, moles)


main()
