from nose.tools import assert_equal


class TestHeight(object):

    def test_height(self):
        root = Node(5)
        assert_equal(height(root), 1)
        insert(root, 2)
        insert(root, 8)
        insert(root, 1)
        insert(root, 3)
        assert_equal(height(root), 3)

        print('Success: test_height')


def main():
    test = TestHeight()
    test.test_height()


if __name__ == '__main__':
    main()