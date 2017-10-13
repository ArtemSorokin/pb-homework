def f(n):
    l = [i for i in range(1, n+1) if n//i * i == n]
    return 'yes' if len(l) == 2 else 'no'

print(f(int(input())))
