from nose.tools import assert_equal


class TestReverse(object):

    def test_reverse(self):
        assert_equal(list_of_chars(None), None)
        assert_equal(list_of_chars(['']), [''])
        assert_equal(list_of_chars(
            ['f', 'o', 'o', ' ', 'b', 'a', 'r']),
            ['r', 'a', 'b', ' ', 'o', 'o', 'f'])
        print('Success: test_reverse')


def main():
    test = TestReverse()
    test.test_reverse()


if __name__ == '__main__':
    main()