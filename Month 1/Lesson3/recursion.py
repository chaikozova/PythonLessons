
def factorial(n, result=1):
    print(n)
    if n == 1:
        return result
    else:
        result = result * n
        return factorial(n-1, result)

print(factorial(10))

