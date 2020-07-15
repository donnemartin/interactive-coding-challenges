import unittest


class TestSolution(unittest.TestCase):

    def test_length_longest_path(self):
        solution = Solution()
        self.assertRaises(TypeError, solution.length_longest_path, None)
        self.assertEqual(solution.length_longest_path(''), 0)
        file_system = 'dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext'
        expected = 32
        self.assertEqual(solution.length_longest_path(file_system), expected)
        print('Success: test_length_longest_path')


def main():
    test = TestSolution()
    test.test_length_longest_path()


if __name__ == '__main__':
    main()
