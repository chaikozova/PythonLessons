
with open('data.txt', 'w') as file:
    file.write('12')

with open('data.txt', 'r') as file:
    print(file.read())

with open('data.txt', 'a') as file:
    file.write('32')

with open('data.txt', 'r') as file:
    print(file.read())
