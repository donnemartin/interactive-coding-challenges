from nose.tools import assert_equal


class TestReverseWords(object):

    def test_reverse(self, func):
        assert_equal(func(None), None)
        assert_equal(func(['']), [''])
        assert_equal(func(
            ['f', 'o', 'o', ' ', 'b', 'a', 'r']),
            ['o', 'o', 'f', ' ', 'r', 'a', 'b'])
        print('Success: test_reverse')


def main():
    test = TestReverseWords()
    reverse_string = ReverseWords()
    test.test_reverse(reverse_string.reverse)


if __name__ == '__main__':
    main()
