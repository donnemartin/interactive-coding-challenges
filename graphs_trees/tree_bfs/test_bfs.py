from __future__ import print_function
from nose.tools import assert_equal


class TestBfs(object):

    def test_bfs(self):
        root = Node(5)
        root.insert(2)
        root.insert(8)
        root.insert(1)
        root.insert(3)

        with captured_output() as (out, err):
            root.bfs(sys.stdout.write)
            assert_equal(out.getvalue().strip(), '52813')

        print('Success: test_bfs')


def main():
    test = TestBfs()
    test.test_bfs()


if __name__ == '__main__':
    main()