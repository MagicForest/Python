import  exercise_7_4

def test_build_dict_with_two_list():
    assert {1:'abc', 2:'def', 3:'ghi'} ==  exercise_7_4.build_dict_with_two_list( [i for i in range(1, 4)],
                                                                                  ['abcdefghi'[i: i+3] for i in range(0, 9, 3)])


def test():
    test_build_dict_with_two_list()


if __name__ == '__main__':
    test()