from nose.tools import assert_equal, assert_raises


class TestSolution(object):

    def test_longest_substr(self):
        solution = Solution()
        assert_raises(TypeError, solution.longest_substr, None)
        assert_equal(solution.longest_substr('', k=3), 0)
        assert_equal(solution.longest_substr('abcabcdefgghiij', k=3), 6)
        assert_equal(solution.longest_substr('abcabcdefgghighij', k=3), 7)
        print('Success: test_longest_substr')


def main():
    test = TestSolution()
    test.test_longest_substr()


if __name__ == '__main__':
    main()