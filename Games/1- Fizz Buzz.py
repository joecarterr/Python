for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        # divisible by 3 and 5
        print("Fizz Buzz")
    elif number % 5 == 0:
        # divisible by 5
        print("Fizz")
    elif number % 3 == 0:
        # divisible by 3
        print("Buzz")
    else:
        print(f"Number was: {number}")
