from nose.tools import assert_equal, assert_raises


class TestPairParentheses(object):

    def test_pair_parentheses(self):
        parentheses = Parentheses()
        assert_raises(TypeError, parentheses.find_pair, None)
        assert_raises(ValueError, parentheses.find_pair, -1)
        assert_equal(parentheses.find_pair(0), [])
        assert_equal(parentheses.find_pair(1), ['()'])
        assert_equal(parentheses.find_pair(2), ['(())',
                                                '()()'])
        assert_equal(parentheses.find_pair(3), ['((()))',
                                                '(()())',
                                                '(())()',
                                                '()(())',
                                                '()()()'])
        print('Success: test_pair_parentheses')


def main():
    test = TestPairParentheses()
    test.test_pair_parentheses()


if __name__ == '__main__':
    main()