import unittest


class TestFindMagicIndex(unittest.TestCase):

    def test_find_magic_index(self):
        magic_index = MagicIndex()
        self.assertEqual(magic_index.find_magic_index(None), -1)
        self.assertEqual(magic_index.find_magic_index([]), -1)
        array = [-4, -2, 2, 6, 6, 6, 6, 10]
        self.assertEqual(magic_index.find_magic_index(array), 2)
        array = [-4, -2, 1, 6, 6, 6, 6, 10]
        self.assertEqual(magic_index.find_magic_index(array), 6)
        array = [-4, -2, 1, 6, 6, 6, 7, 10]
        self.assertEqual(magic_index.find_magic_index(array), -1)
        print('Success: test_find_magic')


def main():
    test = TestFindMagicIndex()
    test.test_find_magic_index()


if __name__ == '__main__':
    main()
