from nose.tools import assert_equal, assert_raises


class TestSolution(object):

    def test_format_license_key(self):
        solution = Solution()
        assert_raises(TypeError, solution.format_license_key, None, None)
        license_key = '---'
        k = 3
        expected = ''
        assert_equal(solution.format_license_key(license_key, k), expected)
        license_key = '2-4A0r7-4k'
        k = 3
        expected = '24-A0R-74K'
        assert_equal(solution.format_license_key(license_key, k), expected)
        license_key = '2-4A0r7-4k'
        k = 4
        expected = '24A0-R74K'
        assert_equal(solution.format_license_key(license_key, k), expected)
        print('Success: test_format_license_key')

def main():
    test = TestSolution()
    test.test_format_license_key()


if __name__ == '__main__':
    main()