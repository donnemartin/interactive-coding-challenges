from nose.tools import assert_true
from nose.tools import raises


class TestTrie(object):       

    def test_trie(self):
        trie = Trie()

        print('Test: Insert')
        words = ['a', 'at', 'has', 'hat', 'he',
                 'me', 'men', 'mens', 'met']
        for word in words:
            trie.insert(word)
        for word in trie.list_words():
            assert_true(trie.find(word) is not None)
            
        print('Test: Remove me')
        trie.remove('me')
        words_removed = ['me']
        words = ['a', 'at', 'has', 'hat', 'he',
                 'men', 'mens', 'met']
        for word in words:
            assert_true(trie.find(word) is not None)
        for word in words_removed:
            assert_true(trie.find(word) is None)

        print('Test: Remove mens')
        trie.remove('mens')
        words_removed = ['me', 'mens']
        words = ['a', 'at', 'has', 'hat', 'he',
                 'men', 'met']
        for word in words:
            assert_true(trie.find(word) is not None)
        for word in words_removed:
            assert_true(trie.find(word) is None)

        print('Test: Remove a')
        trie.remove('a')
        words_removed = ['a', 'me', 'mens']
        words = ['at', 'has', 'hat', 'he',
                 'men', 'met']
        for word in words:
            assert_true(trie.find(word) is not None)
        for word in words_removed:
            assert_true(trie.find(word) is None)

        print('Test: Remove has')
        trie.remove('has')
        words_removed = ['a', 'has', 'me', 'mens']
        words = ['at', 'hat', 'he',
                 'men', 'met']
        for word in words:
            assert_true(trie.find(word) is not None)
        for word in words_removed:
            assert_true(trie.find(word) is None)

        print('Success: test_trie')

    @raises(Exception)
    def test_trie_remove_invalid(self):
        print('Test: Remove from empty trie')
        trie = Trie()
        assert_true(trie.remove('foo') is None) 


def main():
    test = TestTrie()
    test.test_trie()
    test.test_trie_remove_invalid()


if __name__ == '__main__':
    main()