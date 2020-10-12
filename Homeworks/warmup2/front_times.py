def front_times(str, n):
    length = 3
    if length > len(str):
        length = len(str)
    front = str[:length]

    print(n * front)


front_times("Chocolate", 2)
front_times("Marmelade", 3)
