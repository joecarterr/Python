from art import logo, vs
from game_data import data
import random

def get_account():
    return random.choice(data)

def format_name(name):
    name_of_celebrity = name["name"]
    job = name["description"]
    return f"{name_of_celebrity}, a {job}"

def check_answer(user_guess, account1, account2):
    if account1["follower_count"] > account2["follower_count"]:
        return user_guess == "A"
    else:
        return user_guess == "B"

def game():
    print(logo)
    score = 0
    game_should_continue = True
    random_account_1 = get_account()
    random_account_2 = get_account()
    while game_should_continue:
        random_account_1 = random_account_2
        random_account_2 = get_account()

        while random_account_1 == random_account_2:
            random_account_2 = get_account()
        print(f"Compare A: {format_name(name=random_account_1)}")
        print(vs)
        print(f"B: {format_name(name=random_account_2)}")

        guess = input("Who do you think has more followers?: ")
        is_correct = check_answer(user_guess=guess, account1=random_account_1, account2=random_account_2)
        
        if is_correct:
            score += 1
            print(f"Well done! You were correct. Your score is now {score}.")
        else:
            game_should_continue = False
            print(f"Sorry, you were incorrect. Your final score was {score}")
game()
