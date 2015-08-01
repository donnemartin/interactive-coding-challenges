from __future__ import print_function
from nose.tools import assert_equal


class TestDfs(object):

    def test_dfs(self):
        root = Node(5)
        root.insert(2)
        root.insert(8)
        root.insert(1)
        root.insert(3)

        with captured_output() as (out, err):
            root.in_order_traversal(sys.stdout.write)
            assert_equal(out.getvalue().strip(), '12358')

        with captured_output() as (out, err):
            root.pre_order_traversal(sys.stdout.write)
            assert_equal(out.getvalue().strip(), '52138')

        with captured_output() as (out, err):
            root.post_order_traversal(sys.stdout.write)
            assert_equal(out.getvalue().strip(), '13285')

        root = Node(1)
        root.insert(2)
        root.insert(3)
        root.insert(4)
        root.insert(5)

        with captured_output() as (out, err):
            root.in_order_traversal(sys.stdout.write)
            assert_equal(out.getvalue().strip(), '12345')

        with captured_output() as (out, err):
            root.pre_order_traversal(sys.stdout.write)
            assert_equal(out.getvalue().strip(), '12345')

        with captured_output() as (out, err):
            root.post_order_traversal(sys.stdout.write)
            assert_equal(out.getvalue().strip(), '54321')

        print('Success: test_dfs')


def main():
    test = TestDfs()
    test.test_dfs()


if __name__ == '__main__':
    main()