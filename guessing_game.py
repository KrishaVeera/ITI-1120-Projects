import random

def guessnumber(n):
    randomnum = random.randint(1, n)
    guess = 0
    while guess != randomnum:
        guess = int(input("Guess a number between 1 and " + str(n) + ": "))
        if guess < randomnum:
            print("Guess was too low. Try again")
        elif guess > randomnum:
            print("Guess was too high. Try again")

    print("Yay, congrats. You have guessed the number " + str(randomnum) + " correctly!!")
