from nose.tools import assert_equal, assert_raises


class TestMaxProfit(object):

    def test_max_profit(self):
        solution = Solution()
        assert_raises(TypeError, solution.find_max_profit, None)
        assert_raises(ValueError, solution.find_max_profit, [])
        assert_equal(solution.find_max_profit([8, 5, 3, 2, 1]), -1)
        assert_equal(solution.find_max_profit([5, 3, 7, 4, 2, 6, 9]), 7)
        print('Success: test_max_profit')


def main():
    test = TestMaxProfit()
    test.test_max_profit()


if __name__ == '__main__':
    main()