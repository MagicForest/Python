import re


def get_time(a_string):
    return re.findall('\d{4}-\d{2}-\d{2}\s(\d{2}:\d{2}:\d{2})', a_string)

if __name__ == '__main__':
    assert ['10:10:10'] == get_time('abc2017-12-19 10:10:10x')
    assert ['10:10:10', '11:11:11'] == get_time('abc2017-12-19 10:10:10x2016-01-11 11:11:11')
    print 'all passed.'
