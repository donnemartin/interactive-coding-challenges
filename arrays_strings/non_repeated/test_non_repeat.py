from nose.tools import assert_equal


class TestNonRepeat(object):

    def test_non_repeat(self, func):
        assert_equal(func('aabccd'), 'b')
        assert_equal(func('abbccd'), 'a')
        assert_equal(func('aabbadd'), 'a')
        assert_equal(func('aaab'), 'b')
        assert_equal(func('Aabccd'), 'A')
        assert_equal(func('aabbccdd'), None)
        print('Success: test_non_repeat')

def main():
    test = TestNonRepeat()
    nonrepeat = NonRepeat()
    test.test_non_repeat(nonrepeat.non_repeated_char)


if __name__ == '__main__':
    main()
