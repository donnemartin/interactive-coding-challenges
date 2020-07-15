import unittest


class TestMoveZeroes(unittest.TestCase):

    def test_move_zeroes(self):
        solution = Solution()
        self.assertRaises(TypeError, solution.move_zeroes, None)
        array = [0, 1, 0, 3, 12]
        solution.move_zeroes(array)
        self.assertEqual(array, [1, 3, 12, 0, 0])
        array = [1, 0]
        solution.move_zeroes(array)
        self.assertEqual(array, [1, 0])
        array = [0, 1]
        solution.move_zeroes(array)
        self.assertEqual(array, [1, 0])
        array = [0]
        solution.move_zeroes(array)
        self.assertEqual(array, [0])
        array = [1]
        solution.move_zeroes(array)
        self.assertEqual(array, [1])
        array = [1, 1]
        solution.move_zeroes(array)
        self.assertEqual(array, [1, 1])
        print('Success: test_move_zeroes')


def main():
    test = TestMoveZeroes()
    test.test_move_zeroes()


if __name__ == '__main__':
    main()
