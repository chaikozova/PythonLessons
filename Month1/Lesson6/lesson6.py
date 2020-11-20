class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def name(self):
        return self._name

    @property
    # Показ данных
    def age(self):
        return self._age

    @age.setter
    # Получние данных
    def age(self, value):
        if type(value) != int:
            raise ValueError("Возраст не является числом!!!")
        self._age = value

    @name.setter
    def name(self, value):
        if type(value) != str:
            raise ValueError("Имя не является текстом!!!")
        self._name = value


animal1 = Animal("Barbos", 3)
animal1.age = 11
animal1.name = 120
if animal1.age > 10:
    print("Old Animal")

print(animal1.age)
print(animal1.name)
