import sys
# listTest = [1, 2, 3, 4]
# listTest = iter(listTest)
# for it in listTest:
#     print(it)

# while True:
#     try:
#         print(next(listTest))
#     except StopIteration:
#         sys.exit()

"""函数迭代器"""
# class MyNumbers:
#     def __iter__(self):
#         self.a = 2
#         return self
#
#     def __next__(self):
#         x = self.a
#         self.a += 2
#         return x
#
#
# myClass = MyNumbers()
# myClass = iter(myClass)
# print(next(myClass))
# print(next(myClass))

def fibonacci(n): #生成器函数 - 斐波那锲数列
    a, b, counter = 0, 1, 0
    while True:
        if (counter > n):
            return
        yield a
        a, b = b, a + b
        counter += 1


"""fibonacci为迭代器生成类"""
f = fibonacci(10)
for i in f:
    print(i, end=" ")