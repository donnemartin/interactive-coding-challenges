import unittest


class TestBits(unittest.TestCase):

    def test_bits_to_flip(self):
        bits = Bits()
        a = int('11101', base=2)
        b = int('01111', base=2)
        expected = 2
        self.assertEqual(bits.bits_to_flip(a, b), expected)
        print('Success: test_bits_to_flip')


def main():
    test = TestBits()
    test.test_bits_to_flip()


if __name__ == '__main__':
    main()
