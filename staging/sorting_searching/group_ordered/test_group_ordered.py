import unittest


class TestGroupOrdered(unittest.TestCase):
    def test_group_ordered(self, func):

        self.assertEqual(func(None), None)
        print('Success: ' + func.__name__ + " None case.")
        self.assertEqual(func([]), [])
        print('Success: ' + func.__name__ + " Empty case.")
        self.assertEqual(func([1]), [1])
        print('Success: ' + func.__name__ + " Single element case.")
        self.assertEqual(func([1, 2, 1, 3, 2]), [1, 1, 2, 2, 3])
        self.assertEqual(func(['a', 'b', 'a']), ['a', 'a', 'b'])
        self.assertEqual(func([1, 1, 2, 3, 4, 5, 2, 1]), [1, 1, 1, 2, 2, 3, 4, 5])
        self.assertEqual(func([1, 2, 3, 4, 3, 4]), [1, 2, 3, 3, 4, 4])
        print('Success: ' + func.__name__)


def main():
    test = TestGroupOrdered()
    test.test_group_ordered(group_ordered)
    try:
        test.test_group_ordered(group_ordered_alt)
    except NameError:
        # Alternate solutions are only defined
        # in the solutions file
        pass

if __name__ == '__main__':
    main()
