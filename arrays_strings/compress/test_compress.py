from nose.tools import assert_equal


class TestCompress(object):

    def test_compress(self, func):
        assert_equal(func(None), None)
        assert_equal(func(''), '')
        assert_equal(func('AABBCC'), 'AABBCC')
        assert_equal(func('AAABCCDDDD'), 'A3BCCD4')
        assert_equal(func('aaBCCEFFFFKKMMMMMMP taaammanlaarrrr seeeeeeeeek tooo'), 'aaBCCEF4KKM6P ta3mmanlaar4 se9k to3')
        print('Success: test_compress')


def main():
    test = TestCompress()
    test.test_compress(compress_string)


if __name__ == '__main__':
    main()