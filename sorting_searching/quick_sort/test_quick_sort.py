from nose.tools import assert_equal


class TestQuickSort(object):
    def test_quick_sort(self, func):
        print('None input')
        data = None
        sorted_data = func(data)
        assert_equal(sorted_data, None)

        print('Empty input')
        data = []
        sorted_data = func(data)
        assert_equal(sorted_data, [])

        print('One element')
        data = [5]
        sorted_data = func(data)
        assert_equal(sorted_data, [5])

        print('Two or more elements')
        data = [5, 1, 7, 2, 6, -3, 5, 7, -1]
        sorted_data = func(data)
        assert_equal(sorted_data, sorted(data))

        print('Success: test_quick_sort\n')


def main():
    test = TestQuickSort()
    test.test_quick_sort(quick_sort)


if __name__ == '__main__':
    main()