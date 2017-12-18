import re


def replace_email(a_string, new_email):
    return re.sub('\w+@\w+\.\w+', new_email, a_string)

if __name__ == '__main__':
    assert 'wd@wd.wd xx wd@wd.wd b' == replace_email('abc@126.com xx a@133.com b', 'wd@wd.wd')
    assert 'abb' == replace_email('abb', 'wd@wd.wd')
    print 'all passed.'
