from nose.tools import assert_equal, assert_raises


class TestAssignCookie(object):

    def test_assign_cookie(self):
        solution = Solution()
        assert_raises(TypeError, solution.find_content_children, None, None)
        assert_equal(solution.find_content_children([1, 2, 3], 
                                                    [1, 1]), 1)
        assert_equal(solution.find_content_children([1, 2], 
                                                    [1, 2, 3]), 2)
        assert_equal(solution.find_content_children([7, 8, 9, 10], 
                                                    [5, 6, 7, 8]), 2)
        print('Success: test_find_content_children')


def main():
    test = TestAssignCookie()
    test.test_assign_cookie()


if __name__ == '__main__':
    main()