import unittest


class TestAssignCookie(unittest.TestCase):

    def test_assign_cookie(self):
        solution = Solution()
        self.assertRaises(TypeError, solution.find_content_children, None, None)
        self.assertEqual(solution.find_content_children([1, 2, 3], 
                                                    [1, 1]), 1)
        self.assertEqual(solution.find_content_children([1, 2], 
                                                    [1, 2, 3]), 2)
        self.assertEqual(solution.find_content_children([7, 8, 9, 10], 
                                                    [5, 6, 7, 8]), 2)
        print('Success: test_find_content_children')


def main():
    test = TestAssignCookie()
    test.test_assign_cookie()


if __name__ == '__main__':
    main()
