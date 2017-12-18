import re


def match_type(a_string):
    result = re.search("<type '(\w+)'>", a_string)
    if result is not None:
        return result.group(1)

if __name__ == '__main__':
    assert 'int' == match_type("<type 'int'>")
    assert 'float' == match_type("<type 'float'>")
    assert 'builtin_function_or_method' == match_type("<type 'builtin_function_or_method'>")
    assert match_type("<type ''>") is None
    print 'all passed.'
