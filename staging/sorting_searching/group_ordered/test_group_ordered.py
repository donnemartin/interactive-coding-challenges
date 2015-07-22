from nose.tools import assert_equal


class TestGroupOrdered(object):
    def test_group_ordered(self, func):

        assert_equal(func(None), None)
        print('Success: ' + func.__name__ + " None case.")
        assert_equal(func([]), [])
        print('Success: ' + func.__name__ + " Empty case.")
        assert_equal(func([1]), [1])
        print('Success: ' + func.__name__ + " Single element case.")
        assert_equal(func([1, 2, 1, 3, 2]), [1, 1, 2, 2, 3])
        assert_equal(func(['a', 'b', 'a']), ['a', 'a', 'b'])
        assert_equal(func([1, 1, 2, 3, 4, 5, 2, 1]), [1, 1, 1, 2, 2, 3, 4, 5])
        assert_equal(func([1, 2, 3, 4, 3, 4]), [1, 2, 3, 3, 4, 4])
        print('Success: ' + func.__name__)


def main():
    test = TestGroupOrdered()
    test.test_group_ordered(group_ordered)
    try:
        test.test_group_ordered(group_ordered_alt)
    except NameError:
        # Alternate solutions are only defined
        # in the solutions file
        pass

if __name__ == '__main__':
    main()