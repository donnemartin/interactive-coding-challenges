import unittest


class TestSolution(unittest.TestCase):

    def test_is_power_of_two(self):
        solution = Solution()
        self.assertRaises(TypeError, solution.is_power_of_two, None)
        self.assertEqual(solution.is_power_of_two(0), False)
        self.assertEqual(solution.is_power_of_two(1), True)
        self.assertEqual(solution.is_power_of_two(2), True)
        self.assertEqual(solution.is_power_of_two(15), False)
        self.assertEqual(solution.is_power_of_two(16), True)
        print('Success: test_is_power_of_two')


def main():
    test = TestSolution()
    test.test_is_power_of_two()


if __name__ == '__main__':
    main()
