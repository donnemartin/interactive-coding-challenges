from nose.tools import assert_equal


class TestMergeSort(object):
    def test_merge_sort(self):
        print('Empty input')
        data = []
        merge_sort(data)
        assert_equal(data, [])

        print('One element')
        data = [5]
        merge_sort(data)
        assert_equal(data, [5])

        print('Two or more elements')
        data = [5, 1, 7, 2, 6, -3, 5, 7, -1]
        data = merge_sort(data)
        assert_equal(data, sorted(data))

        print('Success: test_merge_sort')


def main():
    test = TestMergeSort()
    test.test_merge_sort()


if __name__ == '__main__':
    main()