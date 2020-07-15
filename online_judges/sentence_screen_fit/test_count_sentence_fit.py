import unittest


class TestSolution(unittest.TestCase):

    def test_count_sentence_fit(self):
        solution = Solution()
        self.assertRaises(TypeError, solution.count_sentence_fit, 
                      None, None, None)
        self.assertRaises(ValueError, solution.count_sentence_fit, 
                      'abc', rows=-1, cols=-1)
        sentence = ["hello", "world"]
        expected = 1
        self.assertEqual(solution.count_sentence_fit(sentence, rows=2, cols=8),
                     expected)
        sentence = ["a", "bcd", "e"]
        expected = 2
        self.assertEqual(solution.count_sentence_fit(sentence, rows=3, cols=6),
                     expected)
        sentence = ["I", "had", "apple", "pie"]
        expected = 1
        self.assertEqual(solution.count_sentence_fit(sentence, rows=4, cols=5),
                     expected)
        print('Success: test_count_sentence_fit')


def main():
    test = TestSolution()
    test.test_count_sentence_fit()


if __name__ == '__main__':
    main()
