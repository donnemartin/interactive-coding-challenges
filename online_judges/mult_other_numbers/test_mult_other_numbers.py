import unittest


class TestMultOtherNumbers(unittest.TestCase):

    def test_mult_other_numbers(self):
        solution = Solution()
        self.assertRaises(TypeError, solution.mult_other_numbers, None)
        self.assertEqual(solution.mult_other_numbers([0]), [])
        self.assertEqual(solution.mult_other_numbers([0, 1]), [1, 0])
        self.assertEqual(solution.mult_other_numbers([0, 1, 2]), [2, 0, 0])
        self.assertEqual(solution.mult_other_numbers([1, 2, 3, 4]), [24, 12, 8, 6])
        print('Success: test_mult_other_numbers')


def main():
    test = TestMultOtherNumbers()
    test.test_mult_other_numbers()


if __name__ == '__main__':
    main()
