def string_bits(str):
    string = ""
    for i in range (len(str)):
        if i % 2 == 0:
            string = string + str[i]
    print(string)


string_bits('Hello')
string_bits('Hi')
string_bits('Heeololeo')