from nose.tools import assert_equal


class TestTree(object):

    def __init__(self):
        self.results = Results()

    def test_tree(self):
        node = Node(5)
        assert_equal(insert(node, 2).data, 2)
        assert_equal(insert(node, 8).data, 8)
        assert_equal(insert(node, 1).data, 1)
        assert_equal(insert(node, 3).data, 3)
        in_order_traversal(node, self.results.add_result)
        assert_equal(str(self.results), '[1, 2, 3, 5, 8]')
        self.results.clear_results()

        node = insert(None, 1)
        assert_equal(insert(node, 2).data, 2)
        assert_equal(insert(node, 3).data, 3)
        assert_equal(insert(node, 4).data, 4)
        insert(node, 5)
        in_order_traversal(node, self.results.add_result)
        assert_equal(str(self.results), '[1, 2, 3, 4, 5]')

        print('Success: test_tree')


def main():
    test = TestTree()
    test.test_tree()


if __name__ == '__main__':
    main()