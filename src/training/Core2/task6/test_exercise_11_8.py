import exercise_11_8

def test_is_leap_year():
    assert exercise_11_8.is_leap_year(1992)
    assert not exercise_11_8.is_leap_year(1900)
    assert exercise_11_8.is_leap_year(2000)


def test_filter_leap_year():
    assert [1992, 1996, 2000] == exercise_11_8.filter_leap_year([1900, 1992, 1996, 1997, 1998, 1999, 2000])
    assert [1992, 1996, 2000] == exercise_11_8.filter_leap_year_by_list_comprehension([1900, 1992, 1996, 1997, 1998, 1999, 2000])


if __name__  == '__main__':
    test_is_leap_year()
    test_filter_leap_year()
