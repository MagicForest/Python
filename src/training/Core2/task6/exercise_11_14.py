def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n-2) + fibonacci(n-1)


def fibonacci_by_reduce(n):
    if n ==1 or n == 2:
        return 1
    else:
        return reduce(lambda  x,y:x+y, map(fibonacci_by_reduce,(n-2, n-1)))
