import re

def pair_word(a_string):
    pattern = '[A-Za-z]+\s[A-Za-z]+'
    result = re.search(pattern, a_string)
    if result is not None:
        return result.group()

if __name__ == '__main__':
    assert 'abc def' == pair_word('abc def')
    assert 'abc def' == pair_word('abc def ghi')
    assert 'def ghi' == pair_word('abc  def ghi')
    assert 'abc def' == pair_word('A  abc def')
    print 'all passed.'
