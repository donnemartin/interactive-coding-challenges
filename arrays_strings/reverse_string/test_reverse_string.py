from nose.tools import assert_equal


class TestReverse(object):

    def test_reverse(self):
        assert_equal(list_of_chars(None), None)
        assert_equal(list_of_chars(['']), [''])
        assert_equal(list_of_chars(
            ['f', 'o', 'o', ' ', 'b', 'a', 'r']),
            ['r', 'a', 'b', ' ', 'o', 'o', 'f'])
        print('Success: test_reverse')

    def test_reverse_inplace(self):
        target_list = ['f', 'o', 'o', ' ', 'b', 'a', 'r']
        list_of_chars(target_list)
        assert_equal(target_list, ['r', 'a', 'b', ' ', 'o', 'o', 'f'])
        print('Success: test_reverse_inplace')


def main():
    test = TestReverse()
    test.test_reverse()
    test.test_reverse_inplace()


if __name__ == '__main__':
    main()