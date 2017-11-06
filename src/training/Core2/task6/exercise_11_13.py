def mult(x, y):
    return x * y

def factorial_loop(n):
    if n == 0:
        return  1
    total = 1
    for i in range(1, n + 1):
        total *= i
    return total


def factorial(n):
    if n == 0:
        return 1;
    else:
        return reduce(mult, range(1, n + 1))


def factorial_by_lambda(n):
    if n == 0:
        return 1;
    else:
        return reduce(lambda x, y: x * y, range(1, n + 1))
