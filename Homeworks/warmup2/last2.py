def last2(str):
    if len(str) < 2:
        print(0)
    else:
        last = str[len(str)-2:]
        x = 0
        for i in range (len(str)-2):
            string = str[i:i+2]
            if string == last:
                x += 1
    print(x)


last2("hixxhi")
last2("xaxxaxaxx")
last2("axxxaaxx")