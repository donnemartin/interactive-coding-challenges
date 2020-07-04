import unittest


class TestCompress(unittest.TestCase):

    def test_compress(self, func):
        self.assertEqual(func(None), None)
        self.assertEqual(func(''), '')
        self.assertEqual(func('AABBCC'), 'AABBCC')
        self.assertEqual(func('AAABCCDDDD'), 'A3BCCD4')
        self.assertEqual(
            func('aaBCCEFFFFKKMMMMMMP taaammanlaarrrr seeeeeeeeek tooo'),
            'aaBCCEF4KKM6P ta3mmanlaar4 se9k to3',
        )
        print('Success: test_compress')


def main():
    test = TestCompress()
    test.test_compress(compress_string)


if __name__ == '__main__':
    main()
