from __future__ import print_function
from nose.tools import assert_equal


class TestDfs(object):

    def test_dfs(self):
        node = Node(5)
        insert(node, 2)
        insert(node, 8)
        insert(node, 1)
        insert(node, 3)

        with captured_output() as (out, err):
            in_order_traversal(node, sys.stdout.write)
            assert_equal(out.getvalue().strip(), '12358')

        with captured_output() as (out, err):
            pre_order_traversal(node, sys.stdout.write)
            assert_equal(out.getvalue().strip(), '52138')

        with captured_output() as (out, err):
            post_order_traversal(node, sys.stdout.write)
            assert_equal(out.getvalue().strip(), '13285')

        node = Node(1)
        insert(node, 2)
        insert(node, 3)
        insert(node, 4)
        insert(node, 5)

        with captured_output() as (out, err):
            in_order_traversal(node, sys.stdout.write)
            assert_equal(out.getvalue().strip(), '12345')

        with captured_output() as (out, err):
            pre_order_traversal(node, sys.stdout.write)
            assert_equal(out.getvalue().strip(), '12345')

        with captured_output() as (out, err):
            post_order_traversal(node, sys.stdout.write)
            assert_equal(out.getvalue().strip(), '54321')

        print('Success: test_dfs')


def main():
    test = TestDfs()
    test.test_dfs()


if __name__ == '__main__':
    main()