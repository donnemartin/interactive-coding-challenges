from nose.tools import assert_equal, assert_raises


class TestRadixSort(object):

    def test_sort(self):
        radix_sort = RadixSort()
        assert_raises(TypeError, radix_sort.sort, None)
        assert_equal(radix_sort.sort([]), [])
        array = [128, 256, 164, 8, 2, 148, 212, 242, 244]
        expected = [2, 8, 128, 148, 164, 212, 242, 244, 256]
        assert_equal(radix_sort.sort(array), expected)
        print('Success: test_sort')


def main():
    test = TestRadixSort()
    test.test_sort()


if __name__ == '__main__':
    main()