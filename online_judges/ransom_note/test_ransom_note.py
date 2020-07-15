import unittest


class TestRansomNote(unittest.TestCase):

    def test_ransom_note(self):
        solution = Solution()
        self.assertRaises(TypeError, solution.match_note_to_magazine, None, None)
        self.assertEqual(solution.match_note_to_magazine('', ''), True)
        self.assertEqual(solution.match_note_to_magazine('a', 'b'), False)
        self.assertEqual(solution.match_note_to_magazine('aa', 'ab'), False)
        self.assertEqual(solution.match_note_to_magazine('aa', 'aab'), True)
        print('Success: test_ransom_note')


def main():
    test = TestRansomNote()
    test.test_ransom_note()


if __name__ == '__main__':
    main()
