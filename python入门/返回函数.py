

def lazy_sum(*arge):
    """求和函数"""
    def sum():
        ax = 0
        for n in arge:
            ax = ax + n
        return ax
    return sum


def create_counter():
    """计数器函数，每次调用它返回递增整数"""
    def plus():
        n = 1
        while True:
            yield n
            n += 1

    x = plus()

    def counter():
        return next(x)
    return counter


# 求和函数使用
# 当我们调用lazy_sum()时，每次调用都会返回一个新的函数，即使传入相同的参数：
f = lazy_sum(1, 4, 5, 2)
# 输出函数  print(f)
# 输出结果  print(f())
c = create_counter()
for i in range(100):
    print(c())
