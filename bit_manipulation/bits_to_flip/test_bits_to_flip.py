from nose.tools import assert_equal


class TestBits(object):

    def test_bits_to_flip(self):
        bits = Bits()
        a = int('11101', base=2)
        b = int('01111', base=2)
        expected = 2
        assert_equal(bits.bits_to_flip(a, b), expected)
        print('Success: test_bits_to_flip')


def main():
    test = TestBits()
    test.test_bits_to_flip()


if __name__ == '__main__':
    main()