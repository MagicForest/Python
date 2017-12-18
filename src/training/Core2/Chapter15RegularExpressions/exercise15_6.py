import re


def matcher(a_string):
    result = re.search('^w{3}\\.\w+\\.com$', a_string)
    if result is not None:
        return result.group()


if __name__ == '__main__':
    assert 'www.yahoo.com' == matcher('www.yahoo.com')
    assert matcher('1www.yahoo.com') is None
    assert matcher('www.yahoo.com1') is None
    assert 'www.1_2w.com' == matcher('www.1_2w.com')
    print 'all passed.'
