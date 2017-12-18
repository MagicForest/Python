import re


def match_email(a_string):
    result = re.search('\w+@\w+\.\w+', a_string)
    if result is not None:
        return  result.group()


if __name__ == '__main__':
    assert 'abc@126.com' == match_email('abc@126.com')
    assert 'ab_c@126.com' == match_email('ab_c@126.com')
    assert match_email('abc@126.') is None
    assert match_email('@126.com') is None
    assert match_email('-@126.com') is None
    print 'all passed.'
