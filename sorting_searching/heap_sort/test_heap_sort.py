from nose.tools import assert_equal, assert_raises


class TestHeapSort(object):

    def test_heap_sort(self):
        sort = HeapSort()

        print('None input')
        assert_raises(TypeError, sort.sort, None)

        print('Empty input')
        assert_equal(sort.sort([]), [])

        print('One element')
        assert_equal(sort.sort([5]), [5])

        print('Two or more elements')
        data = [5, 1, 7, 2, 6, -3, 5, 7, -1]
        assert_equal(sort.sort(data), sorted(data))

        print('Success: test_heap_sort\n')


def main():
    test = TestHeapSort()
    test.test_heap_sort()


if __name__ == '__main__':
    main()