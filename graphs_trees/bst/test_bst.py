from nose.tools import assert_equal


class TestTree(object):

    def __init__(self):
        self.results = Results()

    def test_tree_one(self):
        bst = Bst()
        bst.insert(5)
        bst.insert(2)
        bst.insert(8)
        bst.insert(1)
        bst.insert(3)
        in_order_traversal(bst.root, self.results.add_result)
        assert_equal(str(self.results), '[1, 2, 3, 5, 8]')
        self.results.clear_results()

    def test_tree_two(self):
        bst = Bst()
        bst.insert(1)
        bst.insert(2)
        bst.insert(3)
        bst.insert(4)
        bst.insert(5)
        in_order_traversal(bst.root, self.results.add_result)
        assert_equal(str(self.results), '[1, 2, 3, 4, 5]')

        print('Success: test_tree')


def main():
    test = TestTree()
    test.test_tree_one()
    test.test_tree_two()


if __name__ == '__main__':
    main()