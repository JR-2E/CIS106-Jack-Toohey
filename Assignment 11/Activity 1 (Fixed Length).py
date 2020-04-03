# This program asks how many grades there are,
# gets the grades from the user,
# then finds the lowest, highest, and average score.


def get_number_of_grades():
    print("How many grades are there?")
    number_of_grades = int(input())
    grades = [0] * (number_of_grades)
    return number_of_grades


def calc_avg_grade(number_of_grades, grades):
    avg_count = 0
    grade_sum = 0
    while avg_count < number_of_grades:
        grade_sum = grade_sum + grades[avg_count]
        avg_count = avg_count + 1
    avg_grade = float(grade_sum) / float(number_of_grades)
    return avg_grade


def display_results(avg_grade, low, high):
    print("The average grade is " + str(avg_grade))
    print("The lowest grade is " + str(low))
    print("The highest grade is " + str(high))


def main():
    number_of_grades = get_number_of_grades()
    grades = [None] * (number_of_grades)

    count = 0
    while count != number_of_grades:
        print("Enter a grade.")
        grades[count] = float(input())
        count = count + 1

    grades.sort()
    avg_grade = calc_avg_grade(number_of_grades, grades)
    low = grades[0]
    high = grades[number_of_grades - 1]
    display_results(avg_grade, low, high)


main()
