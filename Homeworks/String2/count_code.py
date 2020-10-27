def count_code(str):
    code = 0
    for i in range(len(str) - 1):
        if str[i + 1] == 'o' and str[i:i + 4:3] == 'ce':
            code += 1
    return code


print(count_code('aaacodebbb'))
print(count_code('codexxcode'))
print(count_code('cozexxcope'))
