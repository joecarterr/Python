def add(*args):
    print(args[0])
    # *args is in type tuple
    total = 0
    for num in args:
        total += num
    return total

# print(add(10, 2, 3, 21, 54))

def calculate(**kwargs):
    # turns it into a dictionary i.e {"add": 5}
    for (key, value) in kwargs.items():
        print(key)
        print(value)

# calculate(add=3, multiply=5)

class Car:

    def __init__(self, **kwargs):
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")
        self.colour = kwargs.get("colour")
        self.seats = kwargs.get("seats")

my_car = Car(make="Nissan", model="GT-R", colour="black", seats=4)
print(my_car.num_of_seats)
