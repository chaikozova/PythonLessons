def missing_char(str, n):
    begin = str[:n]
    end = str[n+1:]
    print(begin + end)


missing_char('kitten', 1)
missing_char('kitten', 0)
missing_char('kitten', 4)