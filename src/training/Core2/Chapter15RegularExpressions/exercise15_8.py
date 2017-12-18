import re


def match_long(a_string):
    result = re.search('-?\d+[Ll]', a_string)
    if result is not None:
        return result.group()

if __name__ == '__main__':
    assert '1L' == match_int('a1Lb')
    assert '12l' == match_int('12la')
    assert '-1l' == match_int('b-1l')
    assert '-1000L' == match_int('d-1000L')
    assert match_int('d-1000') is None
    print 'all passed.'
