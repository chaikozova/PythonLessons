
def sleep_in(weekday, vacation):
    if not weekday or vacation:
        print('We sleep in')
        return True
    else:
        print('We dont sleep in')
        return False


sleep_in(True, False)
sleep_in(False, False)
sleep_in(False, True)
sleep_in(True, True)