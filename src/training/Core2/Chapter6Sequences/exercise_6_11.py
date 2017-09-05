import string

def convert_number_to_ip(number):
    numbers = [number & 0xFF, (number >> 8) & 0xFF, (number >> 16) & 0xFF, (number >> 24) & 0xFF]
    return '.'.join(str(i) for i in reversed(numbers))
    # return '.'.join(str(i) for i in numbers[::-1])


def convert_ip_to_number(ip):
    numbers = [int(i) for i in string.split(ip, '.')]
    number = numbers[-1] + (numbers[-2] << 8) + (numbers[-3] << 16) + (numbers[-4] << 24)
    return number

def test_convert_number_to_ip():
    # 11000000 10101000 00000000 01100101
    assert '192.168.0.101' == convert_number_to_ip(3232235621)
    print '------test_convert_number_to_ip is passed.^__^--------'


def test_convert_ip_to_number():
    assert 3232235621 == convert_ip_to_number('192.168.0.101')
    print '------test_convert_ip_to_number is passed.^__^--------'


def test():
    test_convert_number_to_ip()
    test_convert_ip_to_number()


if __name__ == '__main__':
    test()
