from nose.tools import assert_equal, assert_raises


class TestSolution(object):

    def test_count_sentence_fit(self):
        solution = Solution()
        assert_raises(TypeError, solution.count_sentence_fit, 
                      None, None, None)
        assert_raises(ValueError, solution.count_sentence_fit, 
                      'abc', rows=-1, cols=-1)
        sentence = ["hello", "world"]
        expected = 1
        assert_equal(solution.count_sentence_fit(sentence, rows=2, cols=8),
                     expected)
        sentence = ["a", "bcd", "e"]
        expected = 2
        assert_equal(solution.count_sentence_fit(sentence, rows=3, cols=6),
                     expected)
        sentence = ["I", "had", "apple", "pie"]
        expected = 1
        assert_equal(solution.count_sentence_fit(sentence, rows=4, cols=5),
                     expected)
        print('Success: test_count_sentence_fit')


def main():
    test = TestSolution()
    test.test_count_sentence_fit()


if __name__ == '__main__':
    main()