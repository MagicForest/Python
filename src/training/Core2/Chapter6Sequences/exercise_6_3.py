

def sort_numbers(numbers):
    numbers_len = len(numbers)
    for i in range(0, numbers_len - 1):
        for j in range(i + 1, numbers_len):
           if numbers[i] < numbers[j]:
               numbers[i], numbers[j] = numbers[j], numbers[i]
    return numbers


def test_sort_numbers():
    expected_numbers = [30, 20 , 10]
    assert expected_numbers == sort_numbers([10, 20, 30])
    assert expected_numbers == sort_numbers([30, 20, 10])
    assert expected_numbers == sort_numbers([30, 10, 20])
    assert expected_numbers == sort_numbers([10, 30, 20])
    print '------test_sort_number(number part) is passed.^__^------'

    expected_strings = ['abc', 'abC', 'aBc', 'Abc']
    assert expected_strings == sort_numbers(['abC', 'abc', 'aBc', 'Abc'])
    print '------test_sort_number(string part) is passed.^__^------'


def input_numbers():
    numbers = []
    while True:
        input_string = raw_input('please input number:')
        if not input_string.isdigit():
            break
        else:
            numbers.append(int(input_string))
    print 'original:%s' % numbers
    sort_numbers(numbers)
    print 'sorted:%s' % numbers


def input_strings():
    strings = []
    while True:
        input_string = raw_input('please input string:')
        if not input_string.isalpha():
            break
        else:
            strings.append(input_string)
    print 'original:%s' % strings
    sort_numbers(strings)
    print 'sorted:%s' % strings

if __name__ == "__main__":
    test_sort_numbers()
    input_numbers()
    input_strings()

