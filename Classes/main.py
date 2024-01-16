class Car:
    def __init__(self, seats):
        self.seats = seats

my_car = Car(5)
my_car.seats = (my_car.seats * 2)
print(my_car.seats)