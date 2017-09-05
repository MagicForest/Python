
def split_number(number):
    digits = []
    while True:
        digits.append(number % 10)
        number = number / 10
        if number == 0:
            break
    return tuple(digits)


def show_number(number):
    separator = '-'
    number_mapping_desc = {0:'zero', 1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine',
                           10:'ten', 11:'eleven', 12:'twelve', 13:'thirteen', 14:'fourteen', 15:'fifteen', 16:'sixteen',
                           17:'seventeen', 18:'eighteen', 19:'nineteen', 20:'twenty', 30:'thirty', 40:'forty', 50:'fifty',
                           60:'sixty', 70:'seventy', 80:'eighty', 90:'ninety'}
    if number in number_mapping_desc:
        number_desc = number_mapping_desc.get(number)
    else:
        digits = split_number(number)
        number_len = len(digits)
        if number_len == 2:
            number_desc = number_mapping_desc.get(digits[1] * 10) + separator + number_mapping_desc.get(digits[0])
        elif number_len == 3:
            number_desc = number_mapping_desc.get(digits[2]) + ' hundred'
            if max(digits[0:2]) != 0:
                number_desc += ' and ' +  number_mapping_desc.get(digits[1] * 10) + separator + number_mapping_desc.get(digits[0])
        elif number_len == 4 and max(digits[0:3]) == 0:
            number_desc = 'one thousand'
        else:
            number_desc = 'not supported'
    return number_desc


def test_split_number():
    assert (0,) == split_number(0)
    assert (1, 2) == split_number(21)
    assert (1, 2, 3) == split_number(321)
    assert (0, 0 , 0, 1) == split_number(1000)
    print '---test_split_number is passed.^__^-----'


def test_show_number():
    assert 'zero' == show_number(0)
    assert 'one' == show_number(1)
    assert 'ten' == show_number(10)
    assert 'eleven' == show_number(11)
    assert 'eighty-nine' == show_number(89)
    assert 'one hundred' == show_number(100)
    assert 'one hundred and ninety-nine' == show_number(199)
    assert 'one thousand' == show_number(1000)
    assert 'not supported' == show_number(1001)
    print '---test_show_number is passed.^__^-----'


def test():
    test_split_number()
    test_show_number()


if __name__ == '__main__':
    test()
