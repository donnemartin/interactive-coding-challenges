from nose.tools import assert_equal


class TestDfs(object):

    def __init__(self):
        self.results = Results()

    def test_dfs(self):
        node = Node(5)
        insert(node, 2)
        insert(node, 8)
        insert(node, 1)
        insert(node, 3)

        in_order_traversal(node, self.results.add_result)
        assert_equal(str(self.results), "[1, 2, 3, 5, 8]")
        self.results.clear_results()

        pre_order_traversal(node, self.results.add_result)
        assert_equal(str(self.results), "[5, 2, 1, 3, 8]")
        self.results.clear_results()

        post_order_traversal(node, self.results.add_result)
        assert_equal(str(self.results), "[1, 3, 2, 8, 5]")
        self.results.clear_results()

        node = Node(1)
        insert(node, 2)
        insert(node, 3)
        insert(node, 4)
        insert(node, 5)

        in_order_traversal(node, self.results.add_result)
        assert_equal(str(self.results), "[1, 2, 3, 4, 5]")
        self.results.clear_results()

        pre_order_traversal(node, self.results.add_result)
        assert_equal(str(self.results), "[1, 2, 3, 4, 5]")
        self.results.clear_results()

        post_order_traversal(node, self.results.add_result)
        assert_equal(str(self.results), "[5, 4, 3, 2, 1]")

        print('Success: test_dfs')


def main():
    test = TestDfs()
    test.test_dfs()


if __name__ == '__main__':
    main()