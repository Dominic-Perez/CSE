import random

word_bank = ["Do you like ice cream", "Supercalifragilisticexpialodocious", "Edison High School", "Giraffe", "Enenra",
             "Eight different college playgrounds", "Squidward will hit you with a bat",
             "How much wood could a woodchuck chuck if a woodchuck could chuck wood",
             "Peter Piper picked a peck of pickled peppers",
             "Big Chungus"]

word = random.choice(word_bank)
print(word)
list_word = list(word)

guesses_left = 8
users_chosen_letters = []

while guesses_left > 0:
    # Create Hidden Word
    hidden_word = []
    for letters_in_word in list_word:
        if letters_in_word in users_chosen_letters:
            hidden_word.append(letters_in_word)
        else:
            hidden_word.append("*")

    print("".join(hidden_word))

    # Take input
    users_choice = input("Choose a letter")
    users_chosen_letters.append(users_choice)
    if users_choice not in word:
        guesses_left -= 1
        print("WRONG.")

    if guesses_left == 0:
        print("You lose")

