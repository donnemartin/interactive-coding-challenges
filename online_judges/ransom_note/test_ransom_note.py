from nose.tools import assert_equal, assert_raises


class TestRansomNote(object):

    def test_ransom_note(self):
        solution = Solution()
        assert_raises(TypeError, solution.match_note_to_magazine, None, None)
        assert_equal(solution.match_note_to_magazine('', ''), True)
        assert_equal(solution.match_note_to_magazine('a', 'b'), False)
        assert_equal(solution.match_note_to_magazine('aa', 'ab'), False)
        assert_equal(solution.match_note_to_magazine('aa', 'aab'), True)
        print('Success: test_ransom_note')


def main():
    test = TestRansomNote()
    test.test_ransom_note()


if __name__ == '__main__':
    main()