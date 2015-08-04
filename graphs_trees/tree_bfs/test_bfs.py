from nose.tools import assert_equal


class TestBfs(object):

    def __init__(self):
        self.results = Results()

    def test_bfs(self):
        node = Node(5)
        insert(node, 2)
        insert(node, 8)
        insert(node, 1)
        insert(node, 3)
        bfs(node, self.results.add_result)
        assert_equal(str(self.results), '[5, 2, 8, 1, 3]')

        print('Success: test_bfs')


def main():
    test = TestBfs()
    test.test_bfs()


if __name__ == '__main__':
    main()