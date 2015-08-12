from nose.tools import assert_equal


class TestPairParentheses(object):

    def test_pair_parentheses(self, solution):
        assert_equal(solution(0), set([]))
        assert_equal(solution(1), set(['()']))
        assert_equal(solution(2), set(['(())', 
                                       '()()']))
        assert_equal(solution(3), set(['((()))', 
                                       '(()())', 
                                       '(())()', 
                                       '()(())', 
                                       '()()()']))
        print('Success: test_pair_parentheses')


def main():
    test = TestPairParentheses()
    test.test_pair_parentheses(pair_parentheses)


if __name__ == '__main__':
    main()