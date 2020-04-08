# This program guesses a number of your choice between 0 and 100,
# then displays all of the program's guesses.


def display_directions():
    print("Choose an integer between 0 and 100 in your head. " +
          "This program will try to find it. " +
          "Input 'correct' when the program gets it right, " +
          "or if your number is higher.")


def play_game():
    guesses = []
    guess_amount = 1
    high = 100
    low = 0
    while True:
        guess = (high + low) / 2
        guesses.append(guess)
        print("Guess number " + str(guess_amount) + "." +
              " Is " + str(int(guess)) +
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
                    print("I have found your number! It is " +
                          str(int(guess)) + "!")
                    break
                else:
                    print("Your input was invalid")
    return guesses


def display_results(guesses):
    for output_count in range(len(guesses)):
        print("Guess # " + str((output_count + 1)) +
              " was " + str(int(guesses[output_count])) + ".")


def main():
    display_directions()
    guesses = play_game()
    display_results(guesses)


main()
