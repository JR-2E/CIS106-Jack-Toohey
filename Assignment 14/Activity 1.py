# This program opens a text file saved with a certain format,
# then finds the lowest, highest, and average score.


def get_lines(filename):
    file = open(filename)
    lines = file.readlines()
    return lines


def create_array(filename):
    scores_array = []
    lines = get_lines(filename)
    for x in range(1, len(lines)):
        line = lines[x].split(",")
        scores_array.append(int(line[1]))
    return scores_array


def get_average(scores_array):
    total = 0
    for x in range(0, len(scores_array)):
        score = scores_array[x]
        total = total + int(score)
    average = total / len(scores_array)
    return average


def get_low(scores_array):
    scores_array.sort()
    low = str(min(scores_array))
    return low


def get_high(scores_array):
    scores_array.sort(reverse=True)
    high = str(scores_array[0])
    return high


def display_results(average, low, high):
    print(f"The lowest score is {low}.")
    print(f"The highest score is {high}.")
    print(f"The average of the scores is {average:.2f}.")


def main():
    filename = "scores.txt"
    scores_array = create_array(filename)
    average = get_average(scores_array)
    low = get_low(scores_array)
    high = get_high(scores_array)
    display_results(average, low, high)


main()
