# imports:
from replit import clear
import random
from Games.hangman import hangman_words  # you can import different python files over to one another!
from Games.hangman import hangman_art  # you can import different python files over to one another!
from Games.hangman import hangman_stages  # you can import different python files over to one another!

# hangman art
print(hangman_art.logo)

# stages of the hangman:
stages = hangman_stages.stages

# restart:
end_of_game = False

# setting user lives:
lives = 6

# randomly selecting a word from the list:
chosen_word = random.choice(hangman_words.word_list)

# testing code:
print(f"\npssst the word is {chosen_word}")

# getting the length of the word and displaying it as "_":
display = []
word_length = len(chosen_word)
# loops through the random word and prints out "_" for however many letters are in it:
for char in range(word_length):
    display += "_"
print(display)

# main code:
while not end_of_game:
    # user input:
    user_guess = input("\nPlease enter a letter:\n").lower()
    print(f"You entered the letter {user_guess}\n")

    if user_guess in display:
        print(f"You've already guessed {user_guess}...")
        end_of_game = False

    # if user guess is greater than one character:
    if len(user_guess) > 1:
        print("Sorry the guess has to be a one letter guess!")
        quit()

    # looping through the word and getting its position for where the user has entered a matching word and replacing it
    # with the original "_":
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == user_guess:
            # if the letter in the chosen_word is the same as the user guess then is swaps it:
            # searches through the word one by one and replaces the '_' with the user guessed letter where needed:
            display[position] = letter

        # if the user guess is wrong take a life:
    if user_guess not in chosen_word:
        print(f"Sorry the letter '{user_guess}' was not in the word :(\n")
        print("You just lost one of your lives!")
        lives -= 1
        print(f"You have {lives} lives left!\n")
        end_of_game = False

    print(f"{' '.join(display)}")

    blanks = "_"
    # continuing if there are still blank spaces in the word:
    if blanks in display:
        end_of_game = False
    # checking if there are and '_' left in the word:
    if blanks not in display:
        print("You won!")
        end_of_game = True
    # checking if the users run out of lives and if so ending the programme:
    if lives == 0:
        print("You lost :(")
        end_of_game = True

    print(hangman_stages.stages[lives])
