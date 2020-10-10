# Functions


def sum_of_numbers(*args):  # *args - подстроиться под количество значений
                                        # *args - лист аргументов
    result = 0
    for i in args:
        result += i
    if result > 0:
        print(result)
        return result

    raise ValueError


a = sum_of_numbers(2, 2, 5)
#print(a)

numbers = []

for i in range(6):
    numbers.append(int(input()))    # append добавляет новые значения в лист

sum_of_numbers(*numbers) # * - откроет лист и выдаст все значения

