from nose.tools import assert_equal, assert_raises


class TestAnagrams(object):

    def test_group_anagrams(self):
        anagram = Anagram()
        assert_raises(TypeError, anagram.group_anagrams, None)
        data = ['ram', 'act', 'arm', 'bat', 'cat', 'tab']
        expected = ['ram', 'arm', 'act', 'cat', 'bat', 'tab']
        assert_equal(anagram.group_anagrams(data), expected)

        print('Success: test_group_anagrams')


def main():
    test = TestAnagrams()
    test.test_group_anagrams()


if __name__ == '__main__':
    main()