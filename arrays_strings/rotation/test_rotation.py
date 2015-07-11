from nose.tools import assert_equal


class TestRotation(object):

    def test_rotation(self):
        assert_equal(is_rotation('o', 'oo'), False)
        assert_equal(is_rotation(None, 'foo'), False)
        assert_equal(is_rotation('', 'foo'), False)
        assert_equal(is_rotation('', ''), True)
        assert_equal(is_rotation('foobarbaz', 'barbazfoo'), True)
        print('Success: test_rotation')


def main():
    test = TestRotation()
    test.test_rotation()


if __name__ == '__main__':
    main()