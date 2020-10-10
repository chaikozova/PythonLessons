class Engine:

    def __init__(self, name, hp):
        self.name = name
        self.hp = hp


class Wheels:

    def __init__(self, radius):
        self.radius = radius


class Electronics:

    def __init__(self, country):
        self.country = country


class Car:

    def __init__(self, color, brand, price, data_of_production, engine, wheels, electronics):
        self.color = color
        self.brand = brand
        if isinstance(price, int):
            self.price = price
        else:
            raise ValueError("Price is not integer")
        self.data_of_production = data_of_production
        self.engine = engine
        self.wheels = wheels
        self.electronics = electronics

    def ride(self):
        return "I'm driving"

    def info(self):
        print(f"{self.brand}, {self.color}, {self.price}, {self.data_of_production}, "
              f"{self.engine.name}, {self.engine.hp}, {self.wheels.radius}, "
              f"{self.electronics.country}, {self.ride()}")

    def __str__(self):                  # данный метод отвечает за то, что объект выдаст при принте
        return f"{self.brand}, {self.color}, {self.price}, {self.data_of_production}, " + \
              f"{self.engine.name}, {self.engine.hp}, {self.wheels.radius}, " + \
              f"{self.electronics.country}, {self.ride()}"

class Sedan(Car):

    def __init__(
            self, color, brand, price, data_of_production,
            engine, wheels, electronics, passengers_places, sedan_type):
        super(Sedan, self).__init__(color, brand, price, data_of_production, engine, wheels, electronics)
        self.passengers_places = passengers_places
        self.sedan_type = sedan_type

    def info(self):
        super(Sedan, self).info()
        print(f"{self.sedan_type}, {self.passengers_places}")

    def __str__(self):                  # данный метод отвечает за то, что объект выдаст при принте
        return f"{super(Sedan, self).__str__()}, {self.sedan_type}, {self.passengers_places}"

    def __add__(self, other):
        return f"${self.price + other.price}"


engine = Engine("cool engine", 750)
wheels = Wheels(50)
electronics = Electronics("Japan")


car = Car("red", "ferrari", 123000, "1.10.2020", engine, wheels, electronics)
print(car)

sedan = Sedan("purple", "audi", 12000, "1.10.2020", engine, wheels, electronics, 4, "sport")
sedan2 = Sedan("purple", "audi", 12000, "1.10.2020", engine, wheels, electronics, 4, "sport")
sedan3 = sedan + sedan2
print(sedan3)
