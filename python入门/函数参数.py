import math


def power(x, n=1):
    """求次方"""
    a = x
    for i in range(n-1):
        a *= x
    return a


def quadratis(a, b, c):
    """求一元二次解"""
    up = b * b - 4 * a * c;
    if up < 0:
        print("没有结果！")
        return
    x = math.sqrt(up)
    return (x - b) / (2 * a), (-x - b) / (2 * a)


def person(**syt):
    print(syt["name"])
    print(syt)


def person2(name, age, *, city='shanghai', job):
    print(name, age, city, job)


def product(*x):
    sum = 1
    for i in range(len(x)):
        sum *= x[i]
    return sum


# print(quadratis(1, -2, 0))
# print(power(2, 3))
# person(name='syt', age='111', city='上饶')
# person2('syt', '111', job='jod')
print(product(1, 2, 3, 4))