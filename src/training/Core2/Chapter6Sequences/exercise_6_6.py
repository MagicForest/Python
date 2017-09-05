
def trim(original_string):
    original_string_len = len(original_string)
    begin_index = 0
    end_index = original_string_len
    for i in range(0, original_string_len):
        if original_string[i] != ' ':
            break
        else:
            begin_index = i + 1
    for j in range(original_string_len - 1, begin_index, -1):
        if original_string[j] != ' ':
            break
        else:
            end_index = j
    return original_string[begin_index:end_index]


def test_trim():
    assert 'abc' == trim('abc')
    assert 'abc' == trim('  abc')
    assert '' == trim('  ')
    assert 'abc' == trim('abc  ')
    assert 'abc' == trim('  abc  ')
    assert 'a  b  c' == trim('  a  b  c  ')
    print '---pass---'

if __name__ == '__main__':
    test_trim()
