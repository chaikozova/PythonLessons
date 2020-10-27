def cat_dog(str):
    count_cat = 0
    count_dog = 0
    for i in range(len(str) - 1):
        string = str[i:i + 3]
        if string == 'cat':
            count_cat += 1
        elif string == 'dog':
            count_dog += 1
    if count_cat == count_dog:
        return True
    else:
        return False


print(cat_dog('catdog'))
print(cat_dog('catcat'))
print(cat_dog('1cat1cadodog'))