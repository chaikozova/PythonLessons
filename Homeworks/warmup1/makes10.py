def makes10(a, b):
    if a == 10 or b == 10 or (a+b) == 10:
        return True
    else:
        return False


print(makes10(4, 6))
print(makes10(5, 1))
print(makes10(10, 6))
print(makes10(4, 10))