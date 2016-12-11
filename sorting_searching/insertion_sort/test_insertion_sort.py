from nose.tools import assert_equal, assert_raises


class TestInsertionSort(object):

    def test_insertion_sort(self):
        insertion_sort = InsertionSort()

        print('None input')
        assert_raises(TypeError, insertion_sort.sort, None)

        print('Empty input')
        assert_equal(insertion_sort.sort([]), [])

        print('One element')
        assert_equal(insertion_sort.sort([5]), [5])

        print('Two or more elements')
        data = [5, 1, 7, 2, 6, -3, 5, 7, -1]
        assert_equal(insertion_sort.sort(data), sorted(data))

        print('Success: test_insertion_sort')


def main():
    test = TestInsertionSort()
    test.test_insertion_sort()


if __name__ == '__main__':
    main()