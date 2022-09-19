total = float(input("Please enter the total meal cost:\n"))
people = int(input("How many people would you like to share the cost among?:\n"))

cost = total / people
cost = round(cost, 2)
print(f"Your cost per person is £{cost}")
