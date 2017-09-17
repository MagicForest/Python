import set_task


def test_get_all_sub_set():
    assert set([set(), set('a'), set('b'), set('c'), set('ab'), set('ac'), set('bc'), set('abc')]) == set_task.get_all_sub_set(set('abc'))


if __name__ == '__main__':
    test_get_all_sub_set()
