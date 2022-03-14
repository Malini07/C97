import random

number = random.randint(1,9)
chances = 0

while chances<5:
    guess = int(input("Enter your guess:"))

    if guess == number:
        print("Congratulations you won")
        break

    elif guess<number:
        print("Your guess was too low, guess a number higher than that")

    else:
        print("Your guess was too high, guess a number lower than that")

    chances= chances+1

else:
    print("Sorry there are no chances left and the number is...p",number)