from nose.tools import assert_equal, assert_raises


class TestAddDigits(object):

    def test_add_digits(self, func):
        assert_raises(TypeError, func, None)
        assert_raises(ValueError, func, -1)
        assert_equal(func(0), 0)
        assert_equal(func(9), 9)
        assert_equal(func(138), 3)
        assert_equal(func(65536), 7) 
        print('Success: test_add_digits')


def main():
    test = TestAddDigits()
    solution = Solution()
    test.test_add_digits(solution.add_digits)
    try:
        test.test_add_digits(solution.add_digits_optimized)
    except NameError:
        # Alternate solutions are only defined
        # in the solutions file
        pass


if __name__ == '__main__':
    main()