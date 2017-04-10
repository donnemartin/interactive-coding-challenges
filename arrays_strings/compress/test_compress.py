from nose.tools import assert_equal


class TestCompress(object):

    def test_compress(self, func):
        assert_equal(func(None), None)
        assert_equal(func(''), '')
        assert_equal(func('AABBCC'), 'AABBCC')
        assert_equal(func('AAABCCDDDDE'), 'A3BC2D4E')
        assert_equal(func('BAAACCDDDD'), 'BA3C2D4')
        assert_equal(func('AAABAACCDDDD'), 'A3BA2C2D4')
        print('Success: %s' % func.__name__)


def main():
    test = TestCompress()
    compress_string = CompressString()
    compress_string_2 = CompressString_2()
    test.test_compress(compress_string.compress)
    test.test_compress(compress_string_2.compress_2)


if __name__ == '__main__':
    main()