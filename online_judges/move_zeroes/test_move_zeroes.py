from nose.tools import assert_equal, assert_raises


class TestMoveZeroes(object):

    def test_move_zeroes(self):
        solution = Solution()
        assert_raises(TypeError, solution.move_zeroes, None)
        array = [0, 1, 0, 3, 12]
        solution.move_zeroes(array)
        assert_equal(array, [1, 3, 12, 0, 0])
        array = [1, 0]
        solution.move_zeroes(array)
        assert_equal(array, [1, 0])
        array = [0, 1]
        solution.move_zeroes(array)
        assert_equal(array, [1, 0])
        array = [0]
        solution.move_zeroes(array)
        assert_equal(array, [0])
        array = [1]
        solution.move_zeroes(array)
        assert_equal(array, [1])
        array = [1, 1]
        solution.move_zeroes(array)
        assert_equal(array, [1, 1])
        print('Success: test_move_zeroes')


def main():
    test = TestMoveZeroes()
    test.test_move_zeroes()


if __name__ == '__main__':
    main()