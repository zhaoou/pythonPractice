def sumnum(a, b):
    return a+b


def multi(a, b, sumnum):
    return sumnum(a, b)


def calculate(a):
    def reduce(b):
        return a-b

    def add(c):
        return a+c
    return reduce, add


def reduce(a, b):
    return a-b


def compose(a, b):
    def cal(x, y):
        return a(b(x, y), x)
    return cal


print(compose(sumnum, reduce)(5, 6))

# print(multi(5, 2, sumnum))

#
# func1, func2 = calculate(5)
# print(func1(2))
# print(func2(3))