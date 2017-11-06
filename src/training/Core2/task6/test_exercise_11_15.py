import exercise_11_14


def test_fibonacci():
    assert 1 == exercise_11_14.fibonacci(1)
    assert 1 == exercise_11_14.fibonacci(2)
    assert 2 == exercise_11_14.fibonacci(3)
    assert 8 == exercise_11_14.fibonacci(6)




if __name__ == "__main__":
    test_fibonacci()  
