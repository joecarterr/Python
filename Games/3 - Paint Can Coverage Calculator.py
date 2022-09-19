# import:
import math

# welcome:
print("\n\nWelcome to the Paint Can Coverage Calculator!\n\n")


# main code:
def calculator(paint_coverage):
    start = input("Would you like to begin?:\n").lower()
    if start == "yes" or start == "y":
        print("\nEach can will cover 5m squared e.g.(20 cans will cover a 100m wall)\n")
        wall_height = int(input("Please enter the height of your wall:\n"))
        wall_length = int(input("Please enter the length of the wall:\n"))

        total_area = wall_height * wall_length

        cans_needed = math.ceil(total_area / paint_coverage)
        print(f"You will need {cans_needed} cans of paint to cover your wall")
    else:
        print("Okay, thanks anyways!")
        quit()


calculator(5)
