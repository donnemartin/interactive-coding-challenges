from nose.tools import assert_equal


class TestRotation(object):

    def test_rotation(self):
        rotation = Rotation()
        assert_equal(rotation.is_rotation('o', 'oo'), False)
        assert_equal(rotation.is_rotation(None, 'foo'), False)
        assert_equal(rotation.is_rotation('', 'foo'), False)
        assert_equal(rotation.is_rotation('', ''), True)
        assert_equal(rotation.is_rotation('foobarbaz', 'barbazfoo'), True)
        print('Success: test_rotation')


def main():
    test = TestRotation()
    test.test_rotation()


if __name__ == '__main__':
    main()