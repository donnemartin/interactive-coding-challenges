import unittest


class TestSolution(unittest.TestCase):

    def test_can_win_nim(self):
        solution = Solution()
        self.assertRaises(TypeError, solution.can_win_nim, None)
        self.assertEqual(solution.can_win_nim(1), True)
        self.assertEqual(solution.can_win_nim(2), True)
        self.assertEqual(solution.can_win_nim(3), True)
        self.assertEqual(solution.can_win_nim(4), False)
        self.assertEqual(solution.can_win_nim(7), True)
        self.assertEqual(solution.can_win_nim(40), False)
        print('Success: test_can_win_nim')


def main():
    test = TestSolution()
    test.test_can_win_nim()


if __name__ == '__main__':
    main()
