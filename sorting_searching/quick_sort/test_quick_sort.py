from nose.tools import assert_equal, assert_raises


class TestQuickSort(object):

    def test_quick_sort(self):
        quick_sort = QuickSort()

        print('None input')
        assert_raises(TypeError, quick_sort.sort, None)

        print('Empty input')
        assert_equal(quick_sort.sort([]), [])

        print('One element')
        assert_equal(quick_sort.sort([5]), [5])

        print('Two or more elements')
        data = [5, 1, 7, 2, 6, -3, 5, 7, -1]
        assert_equal(quick_sort.sort(data), sorted(data))

        print('Success: test_quick_sort\n')


def main():
    test = TestQuickSort()
    test.test_quick_sort()


if __name__ == '__main__':
    main()