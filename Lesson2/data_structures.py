
a = ["Roza", 25, "female"]  # List
print(type(a[0]))
print(type(a[-1]))
print(type(a))

for i in a:
    print(i)

names = []

for i in range(5):
    print(names)
    names.append(input())

print(names)

a = ("me", "myself", "I")  # Tuple
                           # нельзя изменять значение
                           # const

dictionary = {"item": ["предмет", "вещь"], "not": "не"}
print(dictionary["item"])

set_a = {"item", "thing", "stuff"}  # хранит только уникальные значения
                                    # set рэндомный порядок

