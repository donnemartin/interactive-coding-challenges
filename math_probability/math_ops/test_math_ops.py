import unittest


class TestMathOps(unittest.TestCase):

    def test_math_ops(self):
        solution = Solution()
        self.assertRaises(TypeError, solution.insert, None)
        solution.insert(5)
        solution.insert(2)
        solution.insert(7)
        solution.insert(9)
        solution.insert(9)
        solution.insert(2)
        solution.insert(9)
        solution.insert(4)
        solution.insert(3)
        solution.insert(3)
        solution.insert(2)
        self.assertEqual(solution.max, 9)
        self.assertEqual(solution.min, 2)
        self.assertEqual(solution.mean, 5)
        self.assertTrue(solution.mode in (2, 9))
        print('Success: test_math_ops')


def main():
    test = TestMathOps()
    test.test_math_ops()


if __name__ == '__main__':
    main()
