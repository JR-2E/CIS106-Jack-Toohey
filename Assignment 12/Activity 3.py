# This program asks how many grades there are,
# gets the grades from the user,
# then finds the lowest, highest, and average score.


def get_grades():
    grades = []
    check = False
    while not check:
        print("Enter a grade.")
        grade = float(input())
        grades.append(grade)
        print("Do you have more grades to enter? (Yes/No)")
        answer = input()
        if answer.lower() == "no":
            check = True
        elif answer.lower() == "yes":
            check = False
    return grades


def calc_avg_grade(grades):
    return sum(grades) / len(grades)


def display_results(avg_grade, low, high, grades):
    output_count = 0
    print("The average grade is " + str(avg_grade))
    print("The lowest grade is " + str(low))
    print("The highest grade is " + str(high))
    print("The grades in highest to lowest order are as follows:")
    while output_count != len(grades):
        print(grades[output_count])
        output_count = output_count + 1


def main():
    grades = get_grades()
    grades.sort(reverse = True)
    avg_grade = calc_avg_grade(grades)
    low = grades[0]
    high = grades[len(grades)-1]
    display_results(avg_grade, low, high, grades)


main()
