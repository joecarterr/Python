import random
possibilities = ["rock", "paper", "scissors"]

should_continue = True
user_score = 0

while should_continue:
    computer_option = random.choice(possibilities)
    user_choice = input("What do you chose? Rock, Paper or Scissors?: ").lower()
    if user_choice == "rock" and computer_option == "paper":
        print("The computer chose", computer_option)
        print("You lose! Your score was,", user_score)
        should_continue = False

    if user_choice == "paper" and computer_option == "rock":
        user_score += 1
        print("The computer chose", computer_option)
        print("You win! Your score was,", user_score)

    if user_choice == "paper" and computer_option == "scissors":
        print("The computer chose", computer_option)
        print("You lose! Your score was,", user_score)
        should_continue = False

    if user_choice == "scissors" and computer_option == "paper":
        user_score += 1
        print("The computer chose", computer_option)
        print("You win! Your score was,", user_score)

    if user_choice == "rock" and computer_option == "scissors":
        user_score += 1
        print("The computer chose", computer_option)
        print("You win! Your score was,", user_score)

    if user_choice == "scissors" and computer_option == "rock":
        print("The computer chose", computer_option)
        print("You lose! Your score was,", user_score)
        should_continue = False

    if user_choice == "paper" and computer_option == "paper":
        print("The computer also chose", computer_option)
        print("You drew! Your score was,", user_score)

    if user_choice == "rock" and computer_option == "rock":
        print("The computer also chose", computer_option)
        print("You drew! Your score was,", user_score)

    if user_choice == "scissors" and computer_option == "scissors":
        print("The computer also chose", computer_option)
        print("You drew! Your score was,", user_score)
