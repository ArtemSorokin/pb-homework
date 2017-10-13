def is_perfect(n):
    s = 0
    for i in range(1, n):
        if n % i == 0:
            s = s + i
    return 'yes' if s == n else 'no'

print(is_perfect(int(input())))
