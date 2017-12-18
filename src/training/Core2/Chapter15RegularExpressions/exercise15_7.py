import re


def match_int(a_string):
    result = re.search('-?\d+', a_string)
    if result is not None:
        return result.group()

if __name__ == '__main__':
    assert '1' == match_int('a1b')
    assert '12' == match_int('12a')
    assert '-1' == match_int('b-1')
    assert '-1000' == match_int('d-1000')
    print 'all passed.'
