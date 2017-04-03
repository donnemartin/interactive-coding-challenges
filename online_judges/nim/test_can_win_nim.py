from nose.tools import assert_equal, assert_raises


class TestSolution(object):

    def test_can_win_nim(self):
        solution = Solution()
        assert_raises(TypeError, solution.can_win_nim, None)
        assert_equal(solution.can_win_nim(1), True)
        assert_equal(solution.can_win_nim(2), True)
        assert_equal(solution.can_win_nim(3), True)
        assert_equal(solution.can_win_nim(4), False)
        assert_equal(solution.can_win_nim(7), True)
        assert_equal(solution.can_win_nim(40), False)
        print('Success: test_can_win_nim')


def main():
    test = TestSolution()
    test.test_can_win_nim()


if __name__ == '__main__':
    main()