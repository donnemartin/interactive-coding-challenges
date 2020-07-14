import unittest


class TestLongestIncreasingSubseq(unittest.TestCase):

    def test_longest_increasing_subseq(self):
        subseq = Subsequence()
        self.assertRaises(TypeError, subseq.longest_inc_subseq, None)
        self.assertEqual(subseq.longest_inc_subseq([]), [])
        seq = [3, 4, -1, 0, 6, 2, 3]
        expected = [-1, 0, 2, 3]
        self.assertEqual(subseq.longest_inc_subseq(seq), expected)
        print('Success: test_longest_increasing_subseq')


def main():
    test = TestLongestIncreasingSubseq()
    test.test_longest_increasing_subseq()


if __name__ == '__main__':
    main()
