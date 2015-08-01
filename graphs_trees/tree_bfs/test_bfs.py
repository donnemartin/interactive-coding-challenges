from __future__ import print_function
from nose.tools import assert_equal


class TestBfs(object):

    def test_bfs(self):
        node = Node(5)
        insert(node, 2)
        insert(node, 8)
        insert(node, 1)
        insert(node, 3)

        with captured_output() as (out, err):
            bfs(node, sys.stdout.write)
            assert_equal(out.getvalue().strip(), '52813')

        print('Success: test_bfs')


def main():
    test = TestBfs()
    test.test_bfs()


if __name__ == '__main__':
    main()