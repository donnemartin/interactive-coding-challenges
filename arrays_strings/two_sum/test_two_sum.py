import unittest


class TestTwoSum(unittest.TestCase):

    def test_two_sum(self):
        solution = Solution()
        self.assertRaises(TypeError, solution.two_sum, None, None)
        self.assertRaises(ValueError, solution.two_sum, [], 0)
        target = 7
        nums = [1, 3, 2, -7, 5]
        expected = [2, 4]
        self.assertEqual(solution.two_sum(nums, target), expected)
        print('Success: test_two_sum')


def main():
    test = TestTwoSum()
    test.test_two_sum()


if __name__ == '__main__':
    main()
