# This program gets test scores, and finds the average
print("How many test scores are there?")
amountOfScores = int(input())
count = 0
totalScore = 0
while count < amountOfScores:
    count = count + 1
    print("Enter test score " + str(count))
    score = int(input())
    totalScore = totalScore + score
averageScore = float(totalScore) / amountOfScores
print("The average test score is " + str(averageScore))
