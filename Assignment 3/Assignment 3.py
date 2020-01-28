# This program converts grams of hydrogen to number of atoms in moles
atomicWeightOfHydrogen = 1.0079
print("Enter grams of hydrogen")
gramsOfHydrogen = float(input())
molesOfHydrogen = gramsOfHydrogen / atomicWeightOfHydrogen
print(str(gramsOfHydrogen) + " Grams of Hydrogen is" + str(molesOfHydrogen) + " moles of Hydrogen")
