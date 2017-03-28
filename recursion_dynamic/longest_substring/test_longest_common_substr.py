from nose.tools import assert_equal, assert_raises


class TestLongestCommonSubstr(object):

    def test_longest_common_substr(self):
        str_comp = StringCompare()
        assert_raises(TypeError, str_comp.longest_common_substr, None, None)
        assert_equal(str_comp.longest_common_substr('', ''), '')
        str0 = 'ABCDEFGHIJ'
        str1 = 'FOOBCDBCDE'
        expected = 'BCDE'
        assert_equal(str_comp.longest_common_substr(str0, str1), expected)
        print('Success: test_longest_common_substr')


def main():
    test = TestLongestCommonSubstr()
    test.test_longest_common_substr()


if __name__ == '__main__':
    main()