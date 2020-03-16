def directions():
    print("Choose an integer between 0 and 100 in your head. This program will try to find it. Input 'correct' when the program gets it right, or if your number is higher.")

def loop():
    guessAmount = 0
    correct = 0
    high = 100
    low = 0
    while correct == 0:
        guess = int((high + low) / 2)
        guessAmount = guessAmount + 1
        print("Guess number " + str(guessAmount) + "." + " Is " + str(guess) + " too high, too low, or is it correct (h,l,c)?")
        answer = input()
        if answer == "High" or answer == "high" or answer == "H" or answer == "h":
            high = guess + 1
        else:
            if answer == "Low" or answer == "low" or answer == "L" or answer == "l":
                low = guess - 1
            else:
                if answer == "Correct" or answer == "correct" or answer == "C" or answer == "c":
                    correct = 1
                    print(f"I have found your number in {guessAmount} guesses! It is {guess}!")
                else:
                    print("Your input was invalid")

# Main
directions()
loop()
