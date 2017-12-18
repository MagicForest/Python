import  re


def match_complex(a_string):
    pattern = '((-?\d+(.\d+)?)([-+]\d+(.\d+)?[jJ]))'
    result = re.search(pattern, a_string)
    if result is not None:
        return result.group()

if __name__ == '__main__':
    assert '1.1+2.2J' == match_complex('1.1+2.2J')
    assert '-1.1-2.2J' == match_complex('-1.1-2.2J')
    print 'all passed.'
