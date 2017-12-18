import re


def match_url(a_string):
    result = re.search('(https?|ftp|file)://[-A-Za-z0-9+&@#/%?=~_|!:,.;]+[-A-Za-z0-9+&@#/%=~_|]', a_string)
    if result is not None:
        return result.group()


if __name__ == '__main__':
    assert 'http://www.zte.com.cn' == match_url('http://www.zte.com.cn')
    assert 'http://www.zte.com.cn&p=1' == match_url('http://www.zte.com.cn&p=1')
    print 'all passed.'
