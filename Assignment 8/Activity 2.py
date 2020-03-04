# This program calculates average test scores.


def get_amount_of_scores():
    print("How many test scores are there?")
    amount_of_scores = int(input())
    return amount_of_scores


def loop(amount_of_scores):
    count = 0
    total_score = 0
    while count < amount_of_scores:
        count = count + 1
        print("Enter test score " + str(count))
        score = input()
        total_score = int(total_score) + int(score)
    average_score = total_score / amount_of_scores
    return average_score


def results(average_score):
    print("The average test score is " + str(average_score))

# Main
amount_of_scores = get_amount_of_scores()
average_score = loop(amount_of_scores)
results(average_score)
