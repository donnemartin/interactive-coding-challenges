import unittest


class TestSumTwo(unittest.TestCase):

    def test_sum_two(self):
        solution = Solution()
        self.assertRaises(TypeError, solution.sum_two, None)
        self.assertEqual(solution.sum_two(5, 7), 12)
        self.assertEqual(solution.sum_two(-5, -7), -12)
        self.assertEqual(solution.sum_two(5, -7), -2)
        print('Success: test_sum_two')


def main():
    test = TestSumTwo()
    test.test_sum_two()


if __name__ == '__main__':
    main()
