def end_other(a, b):
    a = a.lower()
    b = b.lower()
    if a.endswith(b):
        return True
    elif b.endswith(a):
        return True
    else:
        return False


print(end_other('Hiabc', 'abc'))
print(end_other('AbC', 'HiaBc'))
print(end_other('abc', 'abXabc'))