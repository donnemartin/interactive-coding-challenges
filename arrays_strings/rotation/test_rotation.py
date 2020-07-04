import unittest


class TestRotation(unittest.TestCase):

    def test_rotation(self):
        rotation = Rotation()
        self.assertEqual(rotation.is_rotation('o', 'oo'), False)
        self.assertEqual(rotation.is_rotation(None, 'foo'), False)
        self.assertEqual(rotation.is_rotation('', 'foo'), False)
        self.assertEqual(rotation.is_rotation('', ''), True)
        self.assertEqual(rotation.is_rotation('foobarbaz', 'barbazfoo'), True)
        print('Success: test_rotation')


def main():
    test = TestRotation()
    test.test_rotation()


if __name__ == '__main__':
    main()
