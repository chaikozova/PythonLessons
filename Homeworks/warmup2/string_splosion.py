def string_splosion(str):
    string = ""
    for i in range(len(str)):
        string = string + str[:i+1]
    print(string)


string_splosion('Code')
string_splosion('abc')
string_splosion('ab')