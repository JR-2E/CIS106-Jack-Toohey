# This program guesses a number of your choice between 0 and 100,
# then displays all of the program's guesses.


def directions():
    print("Choose an integer between 0 and 100 in your head. " +
          "This program will try to find it. " +
          "Input 'correct' when the program gets it right, " +
          "or if your number is higher.")


def loop():
    guesses = [0] * (69)
    guess_amount = 1
    correct = 0
    high = 100
    low = 0
    count = 0
    while correct == 0:
        guess = (high + low) / 2
        guesses[count] = guess
        count = count + 1
        print("Guess number " + str(guess_amount) + "." +
              " Is " + str(guess) +
              " too high, too low, or is it correct?")
        guess_amount = guess_amount + 1
        answer = input()
        if answer == "High" or answer == "high":
            high = guess
            high = guess + 1
        else:
            if answer == "Low" or answer == "low":
                low = guess
                low = guess - 1
            else:
                if answer == "Correct" or answer == "correct":
                    correct = 1
                    print("I have found your number! It is " +
                          str(guess) + "!")
                else:
                    print("Your input was invalid")
    return guesses, count


def display_results(guesses, count):
    output_count = 0
    for output_count in range(0, count, 1):
        print("Guess # " + str((output_count + 1)) +
              " was " + str(guesses[output_count]) + ".")


def main():
    directions()
    guesses, count = loop()
    display_results(guesses, count)


main()
