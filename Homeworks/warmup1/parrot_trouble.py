def parrot_trouble(talking, hour):
    if (7 > hour or hour > 20) and talking:
        print("We're in trouble")
    else:
        print("We're not in trouble")


parrot_trouble(True, 6)
parrot_trouble(True, 7)
parrot_trouble(False, 6)
parrot_trouble(True, 21)