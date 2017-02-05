from nose.tools import assert_equal


class TestMaximingXor(object):

    def test_maximizing_xor(self):
        solution = Solution()
        assert_equal(solution.max_xor(10, 15), 7)
        print('Success: test_maximizing_xor')


def main():
    test = TestMaximingXor()
    test.test_maximizing_xor()


if __name__ == '__main__':
    main()