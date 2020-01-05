import os


def find_min_max(syt):
    """列表中最大最小值，并且保存在元组中"""
    maxmin = [syt[0], syt[0]]
    for i in range(len(syt)):
        if maxmin[0] < syt[i]:
            maxmin[0] = syt[i]
        if maxmin[1] > syt[i]:
            maxmin[1] = syt[i]
    return tuple(maxmin)


# maxmin = find_min_max([7, 1, 3, 9, 5])
# print(maxmin)
# print([x * x for x in range(1, 11) if x % 2 == 0])
# print([m + n for m in 'syt' for n in 'niu'])
# print([d for d in os.listdir(".")])

L = ['Hello', 'World', 18, 'Apple', None]
L2 = [s.lower() if isinstance(s, str) else str(s) for s in L]
print(L2)
