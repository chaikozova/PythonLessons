lenght = 20
list1 = (i for i in range(lenght))
result = []
list2 = []

for i in range(lenght):
    if i % 2 == 0:
        result.append(i)

print(result)

for i in range(lenght):
    list2.append(i ** 3)

print(list2)