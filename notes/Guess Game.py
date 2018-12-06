import random

a = random.randint(1, 10)
win = False
guesses_left = 5
while guesses_left > 0 and not win:
    answer = int(input("pick a number between 1 and 10"))
    if answer == a:
        print("You win!")
        win = True
    elif answer < a:
        print("The number is higher")
        guesses_left -= 1
    elif answer > a:
        print("The number is lower")
        guesses_left -= 1
    if guesses_left == 0:
        print("You didn't get the number, so you lose!")
        win = True
