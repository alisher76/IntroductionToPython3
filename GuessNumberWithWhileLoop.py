import random

highest = 10
answer = random.randint(1, highest)

print("Please choose number between 1 and {}".format(highest))
guess = 0
numberOfGuesses = 0
numberOfChances = 3

while guess != answer:
    guess = int(input())
    if numberOfChances != 1:
        if guess < answer:
            numberOfGuesses += 1
            numberOfChances -= 1
            print("Please guess higher, you have {} guesses left".format(numberOfChances))
        elif guess > answer:
            numberOfGuesses += 1
            numberOfChances -= 1
            print("Please guess lower, you have {} guesses left".format(numberOfChances))
        else:
            numberOfGuesses += 1
            print("Well done you guessed it")
            if numberOfGuesses == 1:
                print("With the first guess.")
            else:
                print("After {} only guesses.".format(numberOfGuesses))
    else:
        print("Sorry you ran out of tries")
        break
