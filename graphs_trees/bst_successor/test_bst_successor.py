from nose.tools import assert_equal
from nose.tools import raises


class TestBstSuccessor(object):

    @raises(Exception)
    def test_bst_successor_empty(self):
        bst_successor(None)

    def test_bst_successor(self):
        nodes = {}
        node = Node(5)
        nodes[5] = node
        nodes[3] = insert(node, 3)
        nodes[8] = insert(node, 8)
        nodes[2] = insert(node, 2)
        nodes[4] = insert(node, 4)
        nodes[6] = insert(node, 6)
        nodes[12] = insert(node, 12)
        nodes[1] = insert(node, 1)
        nodes[7] = insert(node, 7)
        nodes[10] = insert(node, 10)
        nodes[15] = insert(node, 15)
        nodes[9] = insert(node, 9)

        assert_equal(bst_successor(nodes[4]), 5)
        assert_equal(bst_successor(nodes[5]), 6)
        assert_equal(bst_successor(nodes[8]), 9)
        assert_equal(bst_successor(nodes[15]), None)

        print('Success: test_bst_successor')


def main():
    test = TestBstSuccessor()
    test.test_bst_successor()
    test.test_bst_successor_empty()


if __name__ == '__main__':
    main()