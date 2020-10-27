def extra_end(str):
    if len(str) == 2:
        return str*3
    elif len(str) > 2:
        end = str[2:]
        return end*3
    return 'The word should be longer then 2'


print(extra_end('Hello'))
print(extra_end('ab'))
print(extra_end('Hi'))