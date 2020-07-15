import unittest


class TestMaxProfit(unittest.TestCase):

    def test_max_profit(self):
        solution = Solution()
        self.assertRaises(TypeError, solution.find_max_profit, None)
        self.assertRaises(ValueError, solution.find_max_profit, [])
        self.assertEqual(solution.find_max_profit([8, 5, 3, 2, 1]), -1)
        self.assertEqual(solution.find_max_profit([5, 3, 7, 4, 2, 6, 9]), 7)
        print('Success: test_max_profit')


def main():
    test = TestMaxProfit()
    test.test_max_profit()


if __name__ == '__main__':
    main()
