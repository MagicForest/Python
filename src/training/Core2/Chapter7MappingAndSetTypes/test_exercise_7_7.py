import  exercise_7_7


def test_invert_dict():
    assert {'a':1, 'b':2, 'c':3} == exercise_7_7.invert_dict({1:'a', 2:'b', 3:'c'})


if __name__ == '__main__':
    test_invert_dict()