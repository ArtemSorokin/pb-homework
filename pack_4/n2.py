def derivative(f):
    der = ''

    def split_to_monomials(f):
        l = f.split('+')
        k = []
        for m in l:
            k.append(m.split('-'))
        monomials = []
        for a in k:
            for i in range(len(a)):
                if i > 0:
                    monomials.append('-' + a[i])
                else:
                    monomials.append('+' + a[i])
            pass

        return monomials

    def derivative_mono(m):
        if 'x' not in m:
            d = ''
        else:
            a = m.split('x')
            if a[1] == '':
                d = a[0]
            elif a[1] == '^2':
                d = a[0] + 'x'
            else:
                b = int(a[1][1:])
                d = str(int(a[0])*int(a[1][1:])) + 'x^' + str(int(a[1][1:])-1)
                if a[0][0] != '-':
                    d = '+' + d
        return d

    monomials = split_to_monomials(f)
    for mono in monomials:
        der += derivative_mono(mono)

    return der if der[0] != '+' else der[1:]

# '12x^9+5x^7-17x^5-6x^3+8x^2-26x+179'
print(derivative(str(input())))
