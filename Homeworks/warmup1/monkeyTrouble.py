
def monkey_trouble(a_smile, b_smile):
    if a_smile == b_smile:
        print('We are in trouble')
        return True
    else:
        print('We are not in trouble')
        return False


monkey_trouble(True, True)
monkey_trouble(False, True)
monkey_trouble(True, False)
monkey_trouble(False, False)