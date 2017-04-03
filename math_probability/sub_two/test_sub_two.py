from nose.tools import assert_equal, assert_raises


class TestSubTwo(object):

    def test_sub_two(self):
        solution = Solution()
        assert_raises(TypeError, solution.sub_two, None)
        assert_equal(solution.sub_two(7, 5), 2)
        assert_equal(solution.sub_two(-5, -7), 2)
        assert_equal(solution.sub_two(-5, 7), -12)
        assert_equal(solution.sub_two(5, -7), 12)
        print('Success: test_sub_two')


def main():
    test = TestSubTwo()
    test.test_sub_two()


if __name__ == '__main__':
    main()