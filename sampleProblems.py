# sample problems
# https://mikkegoes.com/python-projects-for-beginners
import math
import random


def isEven(number):
    if number % 2 == 0:
        return True
    else:
        return False




print(isEven(25))


def guessTheNumber():
    randomNum = int(random.random() * 100)
    tries = 0
    found = False
    print(randomNum)

    while tries < 5 and found is False:
        guess = int(input("Guess the number between 0 and 100: "))
        if guess == randomNum:
            found = True
            print("You are right")
        elif guess < randomNum:
            print("Your guess is short")
        else:
            print("Your guess is too large")
        tries += 1
        if found is False and tries < 5:
            print("Try Again")
        elif found is False:
            print("Sorry, you are out of retries")


guessTheNumber()
