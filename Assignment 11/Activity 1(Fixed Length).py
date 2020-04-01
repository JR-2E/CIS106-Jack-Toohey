print("How many grades are there?")
numberOfGrades = int(input())
grades = [0] * (numberOfGrades)

count = 0
while count != numberOfGrades:
    print("Enter a grade.")
    grades[count] = float(input())
    count = count + 1

avgCount = 0
gradeSum = 0
while avgCount < numberOfGrades:
    gradeSum = gradeSum + grades[avgCount]
    avgCount = avgCount + 1
avgGrade = float(gradeSum) / float(numberOfGrades)
print("The average grade is " + str(avgGrade))

grades.sort()
print("The lowest grade is " + str(grades[0]) +".")
print("The highest grade is " + str(grades[numberOfGrades - 1]))
