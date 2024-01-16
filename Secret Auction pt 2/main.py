from replit import clear
from art import logo

print(logo)
continue_bidding = True

bidders = {}
max_bid = 0

def highest_bidder(users_who_bid, top_bid):
    winner = ""
    for bidder in users_who_bid:
        user_bid = users_who_bid[bidder]
        if user_bid > top_bid:
            top_bid = user_bid
            winner = bidder
    print(f"The person with the highest bid was {winner} with a bid of £{top_bid}")

while continue_bidding:
    bidder_name = str(input("Please enter your name: "))
    bid_amount = int(input("Please enter your bid: £"))
    bidders[f"{bidder_name}"] = bid_amount
    more_bidders = str(input("More people to place a bid?: "))
    if more_bidders == "yes":
        clear()
        continue_bidding = True
    else:
        continue_bidding = False
        highest_bidder(users_who_bid=bidders, top_bid=max_bid)
