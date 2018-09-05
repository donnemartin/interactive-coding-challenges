from nose.tools import assert_equal, assert_raises


class TestSumTwo(object):

    def test_sum_two(self):
        solution = Solution()
        assert_raises(TypeError, solution.sum_two, None)
        assert_equal(solution.sum_two(5, 7), 12)
        assert_equal(solution.sum_two(-5, -7), -12)
        assert_equal(solution.sum_two(5, -7), -2)
        print('Success: test_sum_two')


def main():
    test = TestSumTwo()
    test.test_sum_two()


if __name__ == '__main__':
    main()