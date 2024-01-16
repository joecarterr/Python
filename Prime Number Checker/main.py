def prime_checker(number):
    is_prime_number = True
    for num in range(2, number):
        remainder = number % num
        is_prime = remainder == 0
        if is_prime:
            print(f"Your number {number} is not a prime number!")
            is_prime_number = False
    if is_prime_number:
        if number == 1:
            print(f"\nTechnically speaking {number} is not considered to be a prime number!")
        elif number % number == 0 and number % 1 == 0:
            print(f"The number {number} is a prime number!")


prime_checker(number=int(input("Please enter your number: ")))
