from modules.functions import calculator


def print_results(n):
    numbers = []

    for i in range(n):
        numbers.append(int(input()))

    print(calculator(*numbers, operator=input("Enter operator")))


print_results(6)

