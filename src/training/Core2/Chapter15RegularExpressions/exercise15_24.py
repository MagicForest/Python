import re


def get_username_domain(a_string):
    return re.findall('(\w+)@(\w+\.\w+)', a_string)

if __name__ == '__main__':
    assert [('abc', '126.com'), ('bbc', 'bbc.com')] == get_username_domain('abc@126.com xx bbc@bbc.com')
    print 'all passed.'
