import unittest


class TestMergeRanges(unittest.TestCase):

    def test_merge_ranges(self):
        solution = Solution()
        self.assertRaises(TypeError, solution.merge_ranges, None)
        self.assertEqual(solution.merge_ranges([]), [])
        array = [(2, 3), (7, 9)]
        expected = [(2, 3), (7, 9)]
        self.assertEqual(solution.merge_ranges(array), expected)
        array = [(3, 5), (2, 3), (7, 9), (8, 10)]
        expected = [(2, 5), (7, 10)]
        self.assertEqual(solution.merge_ranges(array), expected)
        array = [(2, 3), (3, 5), (7, 9), (8, 10), (1, 11)]
        expected = [(1, 11)]
        self.assertEqual(solution.merge_ranges(array), expected)
        print('Success: test_merge_ranges')


def main():
    test = TestMergeRanges()
    test.test_merge_ranges()


if __name__ == '__main__':
    main()
