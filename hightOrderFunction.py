def sum(a, b):
    return a+b


def multi(a, b):
    return a * b


def calculate(a):
    def reduce(b):
        return a-b

    def add(c):
        return a+c
    return reduce, add


def reduce(a, b):
    return a-b


def compose(a, b, c):
    def cal(x, y):
        return a(b(c(x, y), x), x)
    return cal


def sum_multi(a, b):
    return a+b, a*b


def reduce_multi(a, b):
    return a-b, a*b


def compose2(a, b):
    def cal(x, y):
        return a(b(x, y)[1], y)
    return cal


def sum_multi2(a, b, c):
    return a+b*c


def currying_sum_multi(a):
    def currying1(b):
        def currying2(c):
            return a+b*c  # same as sum_multi2(a, b, c)
        return currying2
    return currying1


def currying_sum_multi(f):
    def currying1(x):
        def currying2(y):
            return f(x, y)
        return currying2
    return currying1


def curry(f):
    def outer(a):
        def inner(b):
            return f(a, b)
        return inner
    return outer


def uncurry(f):
    def inner(a, b):
        return f(a)(b)
    return inner


curry_func = curry(reduce)
# uncurry_func = uncurry(curry_func)
print(uncurry(curry(reduce))(5, 8))

# print(fun_with_1parameter(reduce)(5)(3))

# print(currying_sum_multi(reduce)(3)(5))



# print(currying_sum_multi(1)(2)(3))

# print(compose2(sum_multi, reduce_multi)(2, 5))
# print(compose(sumnum, reduce, multi)(5, 6))

# print(multi(5, 2))

#
# func1, func2 = calculate(5)
# print(func1(2))
# print(func2(3))