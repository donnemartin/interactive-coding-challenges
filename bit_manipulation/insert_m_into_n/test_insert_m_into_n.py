from nose.tools import assert_equal


class TestBit(object):

    def test_insert_m_into_n(self):
        n = int('0000010000111101', base=2)
        m = int('0000000000010011', base=2)
        expected = int('0000010001001101', base=2)
        bits = Bits()
        assert_equal(bits.insert_m_into_n(m, n, i=2, j=6), expected)
        print('Success: test_insert_m_into_n')


def main():
    test = TestBit()
    test.test_insert_m_into_n()


if __name__ == '__main__':
    main()