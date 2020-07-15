import unittest


class TestProdThree(unittest.TestCase):

    def test_prod_three(self):
        solution = Solution()
        self.assertRaises(TypeError, solution.max_prod_three, None)
        self.assertRaises(ValueError, solution.max_prod_three, [1, 2])
        self.assertEqual(solution.max_prod_three([5, -2, 3]), -30)
        self.assertEqual(solution.max_prod_three([5, -2, 3, 1, -1, 4]), 60)
        print('Success: test_prod_three')


def main():
    test = TestProdThree()
    test.test_prod_three()


if __name__ == '__main__':
    main()
