from nose.tools import assert_equal


class TestTree(object):

    def __init__(self):
        self.results = Results()

    def test_tree(self):
        node = Node(5)
        insert(node, 2)
        insert(node, 8)
        insert(node, 1)
        insert(node, 3)
        in_order_traversal(node, self.results.add_result)
        assert_equal(str(self.results), '[1, 2, 3, 5, 8]')
        self.results.clear_results()

        node = Node(1)
        insert(node, 2)
        insert(node, 3)
        insert(node, 4)
        insert(node, 5)
        in_order_traversal(node, self.results.add_result)
        assert_equal(str(self.results), '[1, 2, 3, 4, 5]')

        print('Success: test_tree')


def main():
    test = TestTree()
    test.test_tree()


if __name__ == '__main__':
    main()