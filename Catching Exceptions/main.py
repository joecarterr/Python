try: # attempts this code and catches any errors that may occur:
    with open("Catching Exceptions/a_file.txt", "r") as file:
        print(file.read())
except FileNotFoundError as error_message: # if there is a FileNotFoundError this will occur:
    print(f"There was an error... {error_message}")
    with open("Catching Exceptions/a_file.txt", "a") as file:
        file.write("hey")
else: # if the try section works successfully
    print("Everything worked perfectly")
finally:
    print("You reached the end!")
    # always happens no matter whether there is an error or not