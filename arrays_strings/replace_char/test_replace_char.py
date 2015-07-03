from nose.tools import assert_equal


class TestReplace(object):
    
    def test_replace_char(self, func):
        # | are used to satisfy the constraint that
        # there is enough space in the string to replace
        # ' ' with '%20'
        str0 = None
        str1 = bytearray(' ||')
        str2 = bytearray(' foo bar ||||||')
        str3 = bytearray('foo')
        func(str0, 0)
        func(str1, 1)
        func(str2, 9)
        func(str3, 3)
        assert_equal(str0, None)
        assert_equal(str1, '%20')
        assert_equal(str2, '%20foo%20bar%20')
        assert_equal(str3, 'foo')
        print('Success: test_replace_char')

def main():
    test = TestReplace()
    test.test_replace_char(encode_spaces)
    
if __name__ == '__main__':
    main()