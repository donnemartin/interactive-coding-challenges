from nose.tools import assert_equal


class TestInsertionSort(object):

    def test_insertion_sort(self):
        print('None input')
        data = None
        insertion_sort(data)
        assert_equal(data, None)

        print('Empty input')
        data = []
        insertion_sort(data)
        assert_equal(data, [])

        print('One element')
        data = [5]
        insertion_sort(data)
        assert_equal(data, [5])

        print('Two or more elements')
        data = [5, 1, 7, 2, 6, -3, 5, 7, -1]
        insertion_sort(data)
        assert_equal(data, sorted(data))

        print('Success: test_insertion_sort')


def main():
    test = TestInsertionSort()
    test.test_insertion_sort()


if __name__ == '__main__':
    main()