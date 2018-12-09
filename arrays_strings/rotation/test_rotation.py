from nose.tools import assert_equal


class TestRotation(object):

    def test_rotation(self, func):
        assert_equal(func('o', 'oo'), False)
        assert_equal(func(None, 'foo'), False)
        assert_equal(func('', 'foo'), False)
        assert_equal(func('', ''), True)
        assert_equal(func('foobarbaz', 'barbazfoo'), True)
        print('Success: test_rotation')


def main():
    test = TestRotation()
    rotation = Rotation()
    test.test_rotation(rotation.is_rotation)
    try:
        rotation_in_place = RotationInPlace()
        test.test_rotation(rotation_in_place.is_rotation)
    except NameError:
        # Alternate solutions are only defined
        # in the solutions file
        pass


if __name__ == '__main__':
    main()