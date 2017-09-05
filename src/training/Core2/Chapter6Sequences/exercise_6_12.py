
def findchr(string, char):
   for i, c in enumerate(string):
      if c == char:
         return i
   return -1


def rfindchr(string, char):
    string_len = len(string)
    for i in range(string_len - 1, -1, -1):
        if string[i] == char:
            return i
    return -1


def subchr(string, origchar, newchar):
    new_string = string
    for i, c in enumerate(string):
        if c == origchar:
            new_string = new_string[:i] + str(newchar) + new_string[i+1:]
    return new_string


def test_findchr():
   assert -1 == findchr('abc', 'd')
   assert 0 == findchr('abc', 'a')
   assert 2 == findchr('abc', 'c')
   print '-----test_findchr is passed.^__^-------'


def test_rfindchr():
    assert -1 == rfindchr('abac', 'd')
    assert 2 == rfindchr('abac', 'a')
    assert 0 == rfindchr('abbc', 'a')
    print '-----test_rfindchr is passed.^__^-------'


def test_subchr():
    assert 'abaca' == subchr('abaca', 'd', 'A')
    assert 'A' == subchr('a', 'a', 'A')
    assert 'AbAcA' == subchr('abaca', 'a', 'A')
    print '-----test_subchr is passed.^__^-------'

def test():
   test_findchr()
   test_rfindchr()
   test_subchr()


if __name__ == '__main__':
   test()