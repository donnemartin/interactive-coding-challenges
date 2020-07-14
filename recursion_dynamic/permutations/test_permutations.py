import unittest


class TestPermutations(unittest.TestCase):

    def test_permutations(self):
        permutations = Permutations()
        self.assertEqual(permutations.find_permutations(None), None)
        self.assertEqual(permutations.find_permutations(''), '')
        string = 'AABC'
        expected = [
            'AABC', 'AACB', 'ABAC', 'ABCA',
            'ACAB', 'ACBA', 'BAAC', 'BACA',
            'BCAA', 'CAAB', 'CABA', 'CBAA'
        ]
        self.assertEqual(permutations.find_permutations(string), expected)
        print('Success: test_permutations')


def main():
    test = TestPermutations()
    test.test_permutations()


if __name__ == '__main__':
    main()
