# imports:
import art
import random
from game_data import data

# logo display:
print(art.logo)

def next_name():
    # randomly selecting the names:
    x = random.choice(data)
    y = random.choice(data)
    name_a = x["name"]
    name_b = y["name"]

# randomly selecting the names:
x = random.choice(data)
y = random.choice(data)
name_a = x["name"]
name_b = y["name"]

def game():
    score = 0
    again = True
    while again:

        # user input:
        print(f"Compare A: {name_a}")
        print(art.vs)
        print(f"Against B: {name_b}")
        guess = input("Who do you think has more followers?: ").upper()

        followers_a = x["follower_count"]
        followers_b = y["follower_count"]
        if guess == "A" and followers_a > followers_b:
            score += 1
            print(f"\nWell done! You're correct, {name_a} has {followers_a},000,000 followers.\nYour score is: {score}")
            print("\n" * 10)
            again = True
            next_name()
        elif guess == "B" and followers_a < followers_b:
            score += 1
            print(f"\nWell done! You're correct, {name_b} has {followers_b},000,000 followers.\nYour score is: {score}")
            print("\n" * 10)
            again = True
            next_name()
        else:
            print(f"Sorry you failed with a score of {score}")
            again = False

game()
