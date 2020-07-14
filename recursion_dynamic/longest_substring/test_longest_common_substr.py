import unittest


class TestLongestCommonSubstr(unittest.TestCase):

    def test_longest_common_substr(self):
        str_comp = StringCompare()
        self.assertRaises(TypeError, str_comp.longest_common_substr, None, None)
        self.assertEqual(str_comp.longest_common_substr('', ''), '')
        str0 = 'ABCDEFGHIJ'
        str1 = 'FOOBCDBCDE'
        expected = 'BCDE'
        self.assertEqual(str_comp.longest_common_substr(str0, str1), expected)
        print('Success: test_longest_common_substr')


def main():
    test = TestLongestCommonSubstr()
    test.test_longest_common_substr()


if __name__ == '__main__':
    main()
