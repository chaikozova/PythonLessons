def list_gen(a,b,c):
    list_c = list(range(c))
    list_b = [None] * b
    for i in range(b):
        list_b[i] = list_c
    list_a = [None] * a
    for i in range(a):
        list_a[i] = list_b
        print(list_a[i])



def list_generation(a,b,c):
    result = [[[q for q in range(1, c+1)] for m in range(b)] for i in range(c)]
    #result = []
    #for i in range(a):
    #    m = []
    #    for x in range(b):
    #        n = []
    #        for q in range(c):
    #            n.append(q)
    #        m.append(n)
    #    result.append(m)
    return result


print(list_generation(3, 5, 7))

