def directions():
    print("Choose an integer between 0 and 100 in your head. This program will try to find it. Input 'correct' when the program gets it right, or if your number is higher.")

def loop():
    correct = 0
    high = 100
    low = 0
    while correct == 0:
        guess = (high + low) / 2
        print("Is " + str(guess) + " too high, too low, or is it correct?")
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
                    print("I have found your number! It is " + str(guess) + "!")
                else:
                    print("Your input was invalid")

# Main
directions()
loop()
