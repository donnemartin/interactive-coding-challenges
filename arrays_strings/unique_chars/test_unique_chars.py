from nose.tools import assert_equal


class TestUniqueChars(object):

    def test_unique_chars(self, func):
        assert_equal(func(None), False)
        assert_equal(func(''), True)
        assert_equal(func('foo'), False)
        assert_equal(func('bar'), True)
        print('Success: test_unique_chars')


def main():
    test = TestUniqueChars()
    test.test_unique_chars(unique_chars)
    try:
        test.test_unique_chars(unique_chars_hash)
        test.test_unique_chars(unique_chars_inplace)
    except NameError:
        # Alternate solutions are only defined
        # in the solutions file
        pass


if __name__ == '__main__':
    main()