from nose.tools import assert_equal, assert_raises


class TestFindDiff(object):

    def test_find_diff(self):
        solution = Solution()
        assert_raises(TypeError, solution.find_diff, None)
        assert_equal(solution.find_diff('ab', 'aab'), 'a')
        assert_equal(solution.find_diff('aab', 'ab'), 'a')
        assert_equal(solution.find_diff('abcd', 'abcde'), 'e')
        assert_equal(solution.find_diff('aaabbcdd', 'abdbacade'), 'e')
        assert_equal(solution.find_diff_xor('ab', 'aab'), 'a')
        assert_equal(solution.find_diff_xor('aab', 'ab'), 'a')
        assert_equal(solution.find_diff_xor('abcd', 'abcde'), 'e')
        assert_equal(solution.find_diff_xor('aaabbcdd', 'abdbacade'), 'e')
        print('Success: test_find_diff')


def main():
    test = TestFindDiff()
    test.test_find_diff()


if __name__ == '__main__':
    main()