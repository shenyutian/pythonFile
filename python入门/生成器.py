def triangle(n):
    d = [1]
    for i in range(n):
        yield d
        d = [0] + d + [0]
        d = [d[i] + d[i+1] for i in range(len(d) - 1)]
    pass


def odd():
    for i in range(10):
        yield 1
        yield 2
        yield i


# odd = odd()
# for i in odd:
    # print(i)
ts = triangle(6)
for t in ts:
    print(t)
