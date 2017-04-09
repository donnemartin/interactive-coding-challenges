# %load test_remove_chars.py
from nose.tools import assert_equal


class TestRemoveChars(object):

    def test_remove_chars(self, string, func):
        assert_equal(func(string, None), False)
        assert_equal(func(string, ''), 'Python is great')
        assert_equal(func(string, 'y'), 'Pthon is great')
        assert_equal(func(string, 'tP'), 'yhon is grea')
        print('Success: test_remove_chars')


def main():
    test = TestRemoveChars()
    remove_chars = RemoveChars()
    string = 'Python is great'
    test.test_remove_chars(string, remove_chars.remove_chars)


if __name__ == '__main__':
    main()
