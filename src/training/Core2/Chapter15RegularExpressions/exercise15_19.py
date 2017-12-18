import re


def match_time(a_string):
    # yyyy-MM-dd HH:mm:ss
    return re.findall('\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}:\d{2}', a_string)

if __name__ == '__main__':
    assert ['2017-12-19 10:10:10'] == match_time('abc2017-12-19 10:10:10x')
    assert ['2017-12-19 10:10:10', '2016-11-11 11:11:11'] == match_time('abc2017-12-19 10:10:10x2016-11-11 11:11:11')
    assert [] == match_time('abc2017-12-19 10:10:1')
    assert [] == match_time('abc2017-12-19 10:10:')
    print 'all passed.'

