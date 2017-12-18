import re

def python_identifies(a_string):
    pattern = '[_a-zA-Z]\w*'
    return re.match(pattern, a_string)

if __name__ == '__main__':
    assert python_identifies('a')
    assert python_identifies('a_')
    assert python_identifies('a3')
    assert python_identifies('_')
    assert python_identifies('_a')
    assert not python_identifies('1abc')
    print 'all passed.'
