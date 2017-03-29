from nose.tools import assert_equal, assert_raises


class TestSolution(object):

    def test_is_power_of_two(self):
        solution = Solution()
        assert_raises(TypeError, solution.is_power_of_two, None)
        assert_equal(solution.is_power_of_two(0), False)
        assert_equal(solution.is_power_of_two(1), True)
        assert_equal(solution.is_power_of_two(2), True)
        assert_equal(solution.is_power_of_two(15), False)
        assert_equal(solution.is_power_of_two(16), True)
        print('Success: test_is_power_of_two')


def main():
    test = TestSolution()
    test.test_is_power_of_two()


if __name__ == '__main__':
    main()