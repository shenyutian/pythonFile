

def fact(n):
    # if n > 1:
    #     return n * fact(n-1)
    # else:
    #     return 1
    return fact_iter(n, 1)


def fact_iter(num, product):
    """尾递归调用"""
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)


def move(n, a, b, c):
    """汉诺塔移动 n代表盘子数量"""
    if n == 1:
        print(a, "-->", c)
    else:
        move(n-1, a, c, b)
        move(1, a, b, c)
        move(n-1, b, a, c)


# print(fact(5))
move(4, 'A', 'B', 'C')