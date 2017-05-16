from nose.tools import assert_equal, assert_raises


class TestLongestCommonSubseq(object):

    def test_longest_common_subseq(self):
        str_comp = StringCompare()
        assert_raises(TypeError, str_comp.longest_common_subseq, None, None)
        assert_equal(str_comp.longest_common_subseq('', ''), '')
        str0 = 'ABCDEFGHIJ'
        str1 = 'FOOBCDBCDE'
        expected = 'BCDE'
        assert_equal(str_comp.longest_common_subseq(str0, str1), expected)
        print('Success: test_longest_common_subseq')


def main():
    test = TestLongestCommonSubseq()
    test.test_longest_common_subseq()


if __name__ == '__main__':
    main()
