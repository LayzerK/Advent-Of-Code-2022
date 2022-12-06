with open('inputday4.txt', 'r') as data:
    f = 0
    for i in data:
        a, b = i.split(',')
        print(a, b)
        p, q = map(int, a.split('-'))
        print(p, q)
        r, s = map(int, b.split('-'))
        print(r, s)
        if q >= r and s >= p:
            f += 1
    print(f)
