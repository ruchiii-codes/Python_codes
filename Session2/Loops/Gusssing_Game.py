import random
jackpot = random.randint(1,100)

gusse = int(input("Guess the number between 1 and 100: "))
counter = 1

while gusse != jackpot:
    if gusse < jackpot:
        print("Too low! Guess again.")
    elif gusse > jackpot:
        print("Too high! Guess again.")
    gusse = int(input("Enter a number between 1 and 100: "))
    counter += 1

else:
    print("Congratulations! You guessed the number.")
    print("You took", counter, "tries to guess the number.")