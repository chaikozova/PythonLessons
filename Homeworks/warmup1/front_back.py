def front_back(str):
    if len(str) <= 1:
        print(str)
    else:
        middle_of_word = str[1:-1]
        print(str[-1] + middle_of_word + str[0])


front_back('code')
front_back('a')
front_back('abc')