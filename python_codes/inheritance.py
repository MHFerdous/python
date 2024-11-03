class Car:

    @staticmethod
    def start():
        print("Car started")

    @staticmethod
    def stop():
        print("Car stopped")


class Toyota(Car):
    def __init__(self, name):
        self.name = name


car1 = Toyota("ABC")
car2 = Toyota("XYZ")

print(car1.name)
print(car1.start())
