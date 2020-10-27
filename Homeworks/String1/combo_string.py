def combo_string(a, b):
    if len(a) > len(b):
        return b+a+b
    else:
        return a+b+a


print(combo_string('Hello', 'hi'))
print(combo_string('hi', 'Hello'))
print(combo_string('aaa', 'b'))
print(combo_string('', 'b'))
