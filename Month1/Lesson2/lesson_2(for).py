# Цикл
for data in range(5):
    n = input("Цикл 1")
    print(n)
    if n != "":
        for i in range(3):
            n2 = input("Цикл 2")
            if n2 == "":
                pass
            else:
                break
            print(n2)
    else:
        print("Error")