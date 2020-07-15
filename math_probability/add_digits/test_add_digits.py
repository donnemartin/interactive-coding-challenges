import unittest


class TestAddDigits(unittest.TestCase):

    def test_add_digits(self, func):
        self.assertRaises(TypeError, func, None)
        self.assertRaises(ValueError, func, -1)
        self.assertEqual(func(0), 0)
        self.assertEqual(func(9), 9)
        self.assertEqual(func(138), 3)
        self.assertEqual(func(65536), 7) 
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
