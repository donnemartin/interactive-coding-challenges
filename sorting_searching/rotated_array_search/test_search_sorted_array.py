import unittest


class TestArray(unittest.TestCase):

    def test_search_sorted_array(self):
        array = Array()
        self.assertRaises(TypeError, array.search_sorted_array, None)
        self.assertEqual(array.search_sorted_array([3, 1, 2], 0), None)
        self.assertEqual(array.search_sorted_array([3, 1, 2], 0), None)
        data = [10, 12, 14,  1,  3,  5,  6,  7,  8,  9]
        self.assertEqual(array.search_sorted_array(data, val=1), 3)
        data = [ 1,  1,  2,  1,  1,  1,  1,  1,  1,  1]
        self.assertEqual(array.search_sorted_array(data, val=2), 2)
        print('Success: test_search_sorted_array')


def main():
    test = TestArray()
    test.test_search_sorted_array()


if __name__ == '__main__':
    main()
