def shift(l):
    return l[-1:] + l[0:-1]

l1 = input().split()

print(shift(l1))
