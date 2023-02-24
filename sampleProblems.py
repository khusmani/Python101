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

def rockPaperScissor():
    options = ("Rock", "Paper", "Scissor")
    playAgain = True
    while playAgain:
        rand = random.random();
        computerChoice = 0;
        if rand <= 1 / 3:
            computerChoice = 0
        elif rand <= 2 / 3:
            computerChoice = 1
        else:
            computerChoice = 2

        userChoice = int(input("Your Choice (0:Rock, 1:Paper, 2:Scissor)? "))
        # print("{0} {1}".format(computerChoice, userChoice))
        if computerChoice == userChoice:
            print("{0} {1}".format("It's a TIE, both chose", options[computerChoice]))
        elif computerChoice == 0:
            if userChoice == 1:
                print("You win, you chose Paper and Computer chose Rock, Paper wins over Rock")
            elif userChoice == 2:
                print("You lose, you chose Scissor and Computer chose Rock, Rock wins over Scissor")
        elif computerChoice == 1:
            if userChoice == 0:
                print("You lose, you chose Rock and Computer chose Paper, Paper wins over Rock")
            elif userChoice == 2:
                print("You win, you chose Scissor and Computer chose Paper, Scissor wins over Paper")
        elif computerChoice == 2:
            if userChoice == 0:
                print("You win, you chose Rock and Computer chose Scissor, Rock wins over Scissor")
            elif userChoice == 1:
                print("You lose, you chose Paper and Computer chose Scissor, Scissor wins over Paper")

        playAgain = bool(input("Play Again? (Y/N) "))


rockPaperScissor()