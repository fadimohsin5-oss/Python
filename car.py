class Car:
    def __init__(self, brand):
        self.brand = brand

    def drive(self):
        print(self.brand, "is driving.")

my_car = Car("Mum's Toyota")

my_car.drive()