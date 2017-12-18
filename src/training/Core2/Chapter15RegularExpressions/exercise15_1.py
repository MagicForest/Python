import re

def is_recognized(a_string):
    pattern = '[bh][aiu]t'
    return re.match(pattern, a_string) is not None

if __name__ == '__main__':
    assert is_recognized('bat')
    assert is_recognized('bit')
    assert is_recognized('but')
    assert is_recognized('hat')
    assert is_recognized('hit')
    assert is_recognized('hut')

    print '^__^ all passed.'
