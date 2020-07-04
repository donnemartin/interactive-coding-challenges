import unittest


class TestHashMap(unittest.TestCase):

    # TODO: It would be better if we had unit tests for each
    # method in addition to the following end-to-end test
    def test_end_to_end(self):
        hash_table = HashTable(10)

        print("Test: get on an empty hash table index")
        self.assertRaises(KeyError, hash_table.get, 0)

        print("Test: set on an empty hash table index")
        hash_table.set(0, 'foo')
        self.assertEqual(hash_table.get(0), 'foo')
        hash_table.set(1, 'bar')
        self.assertEqual(hash_table.get(1), 'bar')

        print("Test: set on a non empty hash table index")
        hash_table.set(10, 'foo2')
        self.assertEqual(hash_table.get(0), 'foo')
        self.assertEqual(hash_table.get(10), 'foo2')

        print("Test: set on a key that already exists")
        hash_table.set(10, 'foo3')
        self.assertEqual(hash_table.get(0), 'foo')
        self.assertEqual(hash_table.get(10), 'foo3')

        print("Test: remove on a key that already exists")
        hash_table.remove(10)
        self.assertEqual(hash_table.get(0), 'foo')
        self.assertRaises(KeyError, hash_table.get, 10)

        print("Test: remove on a key that doesn't exist")
        self.assertRaises(KeyError, hash_table.remove, -1)

        print('Success: test_end_to_end')


def main():
    test = TestHashMap()
    test.test_end_to_end()


if __name__ == '__main__':
    main()
