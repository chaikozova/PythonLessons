class Repair:
    def repair(self):
        return self.engine + " Repaired" # noqa


class Drive:
    @staticmethod
    def drive():
        return "Driving"


class Vehicle:
    def __init__(self, size):
        self.size = size


class Car(Vehicle, Repair, Drive):
    def __init__(self, size, engine):
        super(Car, self).__init__(size)
        self.engine = engine


car = Car(100, "engine1")
print(car.repair())
print(car.drive())
