from nose.tools import assert_equal


class TestPermutation(object):

    def test_permutation(self, func):
        assert_equal(func(None, 'foo'), False)
        assert_equal(func('', 'foo'), False)
        assert_equal(func('Nib', 'bin'), False)
        assert_equal(func('act', 'cat'), True)
        assert_equal(func('a ct', 'ca t'), True)
        assert_equal(func('dog', 'doggo'), False)
        print('Success: test_permutation')


def main():
    test = TestPermutation()
    permutations = Permutations()
    test.test_permutation(permutations.is_permutation)

    alternate_solutions = []
    try:
        alternate_solutions.append(PermutationsDefaultdict())
        alternate_solutions.append(PermutationsCounter())
    except NameError:
        # Alternate solutions are only defined
        # in the solutions file
        pass
    for permutations_alt in alternate_solutions:
        test.test_permutation(permutations_alt.is_permutation)


if __name__ == '__main__':
    main()