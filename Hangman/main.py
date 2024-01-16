import random
from replit import clear
# stages of the hangman + logo:
from art import stages, logo
# variety of words:
from words import word_list
game_has_ended = False
lives = 6

print(logo)

display = []
guessed_letters = []

# selecting the random word:
chosen_word = random.choice(word_list)
print(chosen_word)

# displaying the starting boxes:
for letter in range(0, len(chosen_word)):
    display += "_"

print(f"The word has {display} letters in it")

# main game:
while not game_has_ended:

    guess = input(str("Please make a guess for a letter: ")).lower()
    clear()

    if len(guess) > 1:
        print("Sorry, your guess must be one letter!")

    if guess in guessed_letters:
        print("You have already guessed this letter")
    guessed_letters += guess

    for position in range(0, len(chosen_word)):
        letter = chosen_word[position]
        if guess == letter:
            display[position] = letter
            print(display)

    if guess not in chosen_word:
        print(f"The letter '{guess}' is not in the word")
        lives -= 1
        print(stages[lives])
        if lives <= 0:
            print("\n\n\nGame over\n\n\n\n\n\n")
            quit()
        print(display)

    if "_" not in display:
        print("You have guessed the entire word!")
        game_has_ended = True
