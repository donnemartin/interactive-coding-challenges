from __future__ import print_function
from nose.tools import assert_equal


class TestTree(object):

    def test_tree(self):
        root = Node(5)
        root.insert(2)
        root.insert(8)
        root.insert(1)
        root.insert(3)

        with captured_output() as (out, err):
            root.in_order_traversal(sys.stdout.write)
            assert_equal(out.getvalue().strip(), '12358')

        root = Node(1)
        root.insert(2)
        root.insert(3)
        root.insert(4)
        root.insert(5)

        with captured_output() as (out, err):
            root.in_order_traversal(sys.stdout.write)
            assert_equal(out.getvalue().strip(), '12345')

        print('Success: test_tree')


def main():
    test = TestTree()
    test.test_tree()


if __name__ == '__main__':
    main()