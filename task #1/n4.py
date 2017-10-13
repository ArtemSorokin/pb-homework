def f(s):
    return 'yes' if s == s[::-1] else 'no'

print(f(str(input())))
