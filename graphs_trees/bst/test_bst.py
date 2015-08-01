from __future__ import print_function
from nose.tools import assert_equal


class TestTree(object):

    def test_tree(self):
        node = Node(5)
        insert(node, 2)
        insert(node, 8)
        insert(node, 1)
        insert(node, 3)

        with captured_output() as (out, err):
            in_order_traversal(node, sys.stdout.write)
            assert_equal(out.getvalue().strip(), '12358')

        node = Node(1)
        insert(node, 2)
        insert(node, 3)
        insert(node, 4)
        insert(node, 5)

        with captured_output() as (out, err):
            in_order_traversal(node, sys.stdout.write)
            assert_equal(out.getvalue().strip(), '12345')

        print('Success: test_tree')


def main():
    test = TestTree()
    test.test_tree()


if __name__ == '__main__':
    main()