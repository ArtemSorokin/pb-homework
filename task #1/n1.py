def arithmetic(a, b, f):
    return eval(str(a) + f + str(b)) if f in ['+', '-', '*', '/'] else 'unknown operation'

print(arithmetic(int(input()), int(input()), str(input())))
