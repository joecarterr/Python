import math


def calculate(height, length):
    area = float(height) * float(length)
    print(f"The total area of the wall is {area}m squared")
    cans_needed = math.ceil(area / 5)
    print(f"You are going to need {cans_needed} cans of paint to paint your wall")


calculate(height=input("What is the height of your wall in meters?: "),
          length=input("What is the length of your wall in meters?: "))
