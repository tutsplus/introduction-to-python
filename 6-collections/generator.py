def fibon(n):
    a = b = 1
    result = []
    for i in range(n):
        result.append(a)
        a,b = b, a + b
    return result

def fibon_g(n):
    a = b = 1
    for i in range(n):
        yield a
        a,b = b, a + b

for x in fibon_g(100000):
    print(x)
