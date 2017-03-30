from nose.tools import assert_equal


class TestBits(object):

    def test_print_binary(self):
        bit = Bits()
        assert_equal(bit.print_binary(None), 'ERROR')
        assert_equal(bit.print_binary(0), 'ERROR')
        assert_equal(bit.print_binary(1), 'ERROR')
        num = 0.625
        expected = '0.101'
        assert_equal(bit.print_binary(num), expected)
        num = 0.987654321
        assert_equal(bit.print_binary(num), 'ERROR')
        print('Success: test_print_binary')


def main():
    test = TestBits()
    test.test_print_binary()


if __name__ == '__main__':
    main()