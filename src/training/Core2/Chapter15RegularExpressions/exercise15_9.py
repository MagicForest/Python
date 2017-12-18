import re


def match_float(a_string):
    result = re.search('-?\d+(.\d+)?', a_string)
    if result is not None:
        return result.group()

if __name__ == '__main__':
    assert '1.1' == match_float('a1.1b')
    assert '12' == match_float('12la')
    assert '-1.23' == match_float('b-1.23l')
    assert '-1000' == match_float('d-1000L')
    print 'all passed.'
