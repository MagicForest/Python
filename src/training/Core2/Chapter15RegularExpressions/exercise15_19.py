import re


def match_time(a_string):
    # yyyy-MM-dd HH:mm:ss
    result = re.search('\d{4}(-\d{2}){2}\s\d{2}(:\d{2}){2}', a_string)
    if result is not None:
        return result.group()

if __name__ == '__main__':
    assert '2017-12-19 10:10:10' == match_time('abc2017-12-19 10:10:10x')
    assert match_time('abc2017-12-19 10:10:1') is None
    assert match_time('abc2017-12-19 10:10:') is None
    print 'all passed.'

