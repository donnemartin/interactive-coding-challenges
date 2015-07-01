from nose.tools import assert_equal


class TestSelectionSort(object):
    
    def test_selection_sort(self, func):
        print('Empty input')
        data = []
        func(data)
        assert_equal(data, [])

        print('One element')
        data = [5]
        func(data)
        assert_equal(data, [5])

        print('Two or more elements')
        data = [5, 1, 7, 2, 6, -3, 5, 7, -1]
        func(data)
        assert_equal(data, sorted(data))
        
        print('Success: test_selection_sort\n')

def main():
    test = TestSelectionSort()
    test.test_selection_sort(selection_sort)
    try:
        test.test_selection_sort(selection_sort_iterative)
    except NameError:
        # Alternate solutions are only defined
        # in the solutions file
        pass

if __name__ == '__main__':
    main()