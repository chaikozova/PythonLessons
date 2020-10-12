def string_match(a, b):
    c = min(len(a), len(b))
    count = 0
    for i in range(c - 1):
        a1 = a[i:i + 2]
        b1 = b[i:i + 2]
        if a1 == b1:
            count += 1
    print(count)


string_match('xxcaazz', 'xxbaaz')
string_match('abc', 'abc')
string_match('abc', 'axc')
