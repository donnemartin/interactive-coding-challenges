from nose.tools import assert_equal, assert_raises


class TestMath(object):

    def test_check_prime(self):
        math = Math()
        assert_raises(TypeError, math.check_prime, None)
        assert_raises(TypeError, math.check_prime, 98.6)
        assert_equal(math.check_prime(0), False)
        assert_equal(math.check_prime(1), False)
        assert_equal(math.check_prime(97), True)
        print('Success: test_check_prime')


def main():
    test = TestMath()
    test.test_check_prime()


if __name__ == '__main__':
    main()