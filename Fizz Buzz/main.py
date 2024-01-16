for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:  # divisible by both three and five
        print("Fizz Buzz!")
    elif number % 3 == 0:  # divisible by only three
        print("Fizz")
    elif number % 5 == 0:  # divisible by only five
        print("Buzz")
    else:
        print(number)
