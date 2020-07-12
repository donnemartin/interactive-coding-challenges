import unittest


class TestBits(unittest.TestCase):

    def test_flip_bit(self):
        bits = Bits()
        self.assertRaises(TypeError, bits.flip_bit, None)
        self.assertEqual(bits.flip_bit(0), 1)
        self.assertEqual(bits.flip_bit(-1), bits.MAX_BITS)
        num = int('00001111110111011110001111110000', base=2)
        expected = 10
        self.assertEqual(bits.flip_bit(num), expected)
        num = int('00000100111011101111100011111011', base=2)
        expected = 9
        self.assertEqual(bits.flip_bit(num), expected)
        num = int('00010011101110111110001111101111', base=2)
        expected = 10
        self.assertEqual(bits.flip_bit(num), expected)
        print('Success: test_print_binary')


def main():
    test = TestBits()
    test.test_flip_bit()


if __name__ == '__main__':
    main()
