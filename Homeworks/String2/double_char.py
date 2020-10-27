def double_char(str):
    double_str = ''
    for i in range(len(str)):
        double_str += (str[i] * 2)
    return double_str


print(double_char('Hello'))
print(double_char('The'))
print(double_char('AAbb'))