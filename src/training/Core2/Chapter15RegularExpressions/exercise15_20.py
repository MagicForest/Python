import re


def get_email(a_string):
    return re.findall('\w+@\w+\.\w+', a_string)

if __name__ == '__main__':
    assert ['abc@126.com', 'a@133.com'] == get_email('abc@126.com xx a@133.com b')
    print 'all passed.'
