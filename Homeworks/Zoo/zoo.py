class Animal:
    def __init__(self, type, age, color):
        self.type = type
        self.age = age
        self.color = color

    def __str__(self):
        return f"type of Animal: {self.type}, Age: {self.age}, Color: {self.color}"


class Monkey(Animal):
    def __init__(self, type, age, color, name, room):
        super(Monkey, self).__init__(type, age, color)
        self.name = name
        self.room = room

    def __str__(self):
        return f"{super(Monkey, self).__str__()}, Name: {self.name}, Room# {self.room}"


class Elephant(Animal):
    def __init__(self, type, age, color, children, family):
        super(Elephant, self).__init__(type, age, color)
        self.children = children
        self.family = family

    def __str__(self):
        return f"{super(Elephant, self).__str__()}, " + \
               f"\nDoes elephant have a family?" + \
               f" - {self.family}" + \
               f"\nDoes elephant have childrens?" + \
               f" - {self.children}"


animal = Animal("Bird", 4, "Black")
print(animal)
monkey = Monkey("Monkey", 5, "Brown", "Abu", 3)
print(monkey)
elephant = Elephant("Elephant", 10, "Grey", True, True)
print(elephant)