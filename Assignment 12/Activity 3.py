# This program asks how many grades there are,
# gets the grades from the user,
# then finds the lowest, highest, and average score.


def get_grades():
    grades = []
    check = False
    print("When promted, enter a grade." +
          "When you are done," +
          "enter any negative number instead of a grade score.")
    while not check:
        print("Enter a grade.")
        grade = float(input())
        if grade < 0:
            check = True
        else:
            grades.append(grade)
    return grades


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
    avg_grade = sum(grades) / len(grades)
    high = grades[0]
    low = grades[len(grades)-1]
    display_results(avg_grade, low, high, grades)


main()
