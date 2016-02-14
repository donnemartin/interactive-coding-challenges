from nose.tools import assert_equal


class TestReverse(object):

    def test_reverse(self):
        assert_equal(reverse_string(None), None)
        assert_equal(reverse_string(['']), [''])
        assert_equal(reverse_string(
            ['f', 'o', 'o', ' ', 'b', 'a', 'r']),
            ['r', 'a', 'b', ' ', 'o', 'o', 'f'])
        print('Success: test_reverse')

    def test_reverse_inplace(self):
        target_list = ['f', 'o', 'o', ' ', 'b', 'a', 'r']
        reverse_string(target_list)
        assert_equal(target_list, ['r', 'a', 'b', ' ', 'o', 'o', 'f'])
        print('Success: test_reverse_inplace')


def main():
    test = TestReverse()
    test.test_reverse()
    test.test_reverse_inplace()


if __name__ == '__main__':
    main()