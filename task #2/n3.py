def fact(a):
    f = 1
    for i in range(a):
        f = f * (i+1)
    return f

def C(m, n):
    return fact(n)/(fact(m)*fact(n-m))

def pasc_inner(n):
    if n > 1:
        pasc_inner(n-1)
    else:
        print(1)
    for m in range(n+1):
        print(int(C(m, n)), end=' ')
    print()

def pasc(n):
    pasc_inner(n-1)

pasc(int(input()))
