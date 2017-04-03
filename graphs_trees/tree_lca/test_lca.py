from nose.tools import assert_equal


class TestLowestCommonAncestor(object):

    def test_lca(self):
        node10 = Node(10)
        node5 = Node(5)
        node12 = Node(12)
        node3 = Node(3)
        node1 = Node(1)
        node8 = Node(8)
        node9 = Node(9)
        node18 = Node(18)
        node20 = Node(20)
        node40 = Node(40)
        node3.left = node1
        node3.right = node8
        node5.left = node12
        node5.right = node3
        node20.left = node40
        node9.left = node18
        node9.right = node20
        node10.left = node5
        node10.right = node9
        root = node10
        node0 = Node(0)
        binary_tree = BinaryTree()
        assert_equal(binary_tree.lca(root, node0, node5), None)
        assert_equal(binary_tree.lca(root, node5, node0), None)
        assert_equal(binary_tree.lca(root, node1, node8), node3)
        assert_equal(binary_tree.lca(root, node12, node8), node5)
        assert_equal(binary_tree.lca(root, node12, node40), node10)
        assert_equal(binary_tree.lca(root, node9, node20), node9)
        assert_equal(binary_tree.lca(root, node3, node5), node5)
        print('Success: test_lca')


def main():
    test = TestLowestCommonAncestor()
    test.test_lca()


if __name__ == '__main__':
    main()