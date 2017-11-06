import exercise_11_13
import exercise_11_12

def test_mult():
    assert 15 == exercise_11_13.mult(3, 5)

def test_factorial_tests():
    test_factorial(exercise_11_13.factorial_loop)
    test_factorial(exercise_11_13.factorial)
    test_factorial(exercise_11_13.factorial_by_lambda)

def test_factorial(factorial_func):
    assert 1 == factorial_func(0)
    assert 1 == factorial_func(1)
    assert 2 == factorial_func(2)
    assert 6 == factorial_func(3)
    assert 24 == factorial_func(4)


if __name__ == "__main__":
    test_mult()
    test_factorial_tests()
    n = 10000
    print exercise_11_12.timeit(exercise_11_13.factorial_loop, n)[0]
    print exercise_11_12.timeit(exercise_11_13.factorial, n)[0]
    print exercise_11_12.timeit(exercise_11_13.factorial_by_lambda, n)[0]
