MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}

def check_amount(total_amount):
    if total_amount < MENU[f"{option}"]["cost"]:
        return "Sorry, you do not have enough money for this"
    else:
        water = resources["water"]
        coffee = resources["coffee"]
        milk = resources["milk"]
        if water >= MENU[f"{option}"]["ingredients"]["water"]:
            if coffee >= MENU[f"{option}"]["ingredients"]["coffee"]:
                if milk >= MENU[f"{option}"]["ingredients"]["milk"]:
                    resources["water"] -= MENU[f"{option}"]["ingredients"]["water"]
                    resources["milk"] -= MENU[f"{option}"]["ingredients"]["milk"]
                    resources["coffee"] -= MENU[f"{option}"]["ingredients"]["coffee"]
                    resources["money"] += total_amount
                    return f"Here is your {option}☕. Enjoy!!"
        else:
            return "Insufficient ingredients"
        


def insert_coins():
    quarters = int(input("How many quarters?: "))
    num_of_quarters = (quarters * 0.25)
    dimes = int(input("How many dime?: "))
    num_of_dime = (dimes * 0.1)
    nickles = int(input("How many nickles?: "))
    num_of_nickles = (nickles * 0.05)
    pennies = int(input("How many pennies?: "))
    num_of_pennies = (pennies * 0.01)
    total = num_of_quarters + num_of_dime + num_of_nickles + num_of_pennies
    if total > MENU[f"{option}"]["cost"]:
        total -= MENU[f"{option}"]["cost"]
        print(f"You inserted too much. Here is £{total}0 back!")
    print(check_amount(total_amount=total))

option = input("What would you like to order? (espresso/latte/cappuccino): ").lower()

if option == "report":
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]
    money = resources["money"]
    print(f"Water: {water}\nMilk: {milk}\nCoffee: {coffee}\nMoney: £{money}")

if option == "espresso":
    insert_coins()

if option == "latte":
    insert_coins()

if option == "capuccino":
    insert_coins()