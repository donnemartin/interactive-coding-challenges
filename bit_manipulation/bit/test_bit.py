from nose.tools import assert_equal


class TestBit(object):

    def test_bit(self):
        number = int('10001110', base=2)
        bit = Bit(number)
        assert_equal(bit.get_bit(index=3), True)
        expected = int('10011110', base=2)
        assert_equal(bit.set_bit(index=4), expected)
        bit = Bit(number)
        expected = int('10000110', base=2)
        assert_equal(bit.clear_bit(index=3), expected)
        bit = Bit(number)
        expected = int('00000110', base=2)
        assert_equal(bit.clear_bits_msb_to_index(index=3), expected)
        bit = Bit(number)
        expected = int('10000000', base=2)
        assert_equal(bit.clear_bits_index_to_lsb(index=3), expected)
        bit = Bit(number)
        assert_equal(bit.update_bit(index=3, value=1), number)
        bit = Bit(number)
        expected = int('10000110', base=2)
        assert_equal(bit.update_bit(index=3, value=0), expected)
        bit = Bit(number)
        expected = int('10001111', base=2)
        assert_equal(bit.update_bit(index=0, value=1), expected)
        print('Success: test_bit')


def main():
    test = TestBit()
    test.test_bit()


if __name__ == '__main__':
    main()