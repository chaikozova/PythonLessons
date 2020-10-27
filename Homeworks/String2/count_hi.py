def count_hi(str):
    count = 0
    for i in range(len(str)-1):
        string = str[i:i+2]
        if string == 'hi':
            count +=1
    return count


print(count_hi('abc hi ho'))
print(count_hi('ABChi hi ho'))
print(count_hi('hi hi'))