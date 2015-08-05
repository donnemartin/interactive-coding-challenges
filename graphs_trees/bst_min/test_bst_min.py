from nose.tools import assert_equal


class TestBstMin(object):

    def test_bst_min(self):
        array = [0, 1, 2, 3, 4, 5, 6]
        root = create_min_bst(array)
        assert_equal(height(root), 3)

        array = [0, 1, 2, 3, 4, 5, 6, 7]
        root = create_min_bst(array)
        assert_equal(height(root), 4)

        print('Success: test_bst_min')


def main():
    test = TestBstMin()
    test.test_bst_min()


if __name__ == '__main__':
    main()