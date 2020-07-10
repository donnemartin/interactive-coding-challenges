import unittest


class TestInvertTree(unittest.TestCase):

    def test_invert_tree(self):
        root = Node(5)
        bst = InverseBst(root)
        node2 = bst.insert(2)
        node3 = bst.insert(3)
        node1 = bst.insert(1)
        node7 = bst.insert(7)
        node6 = bst.insert(6)
        node9 = bst.insert(9)
        result = bst.invert_tree()
        self.assertEqual(result, root)
        self.assertEqual(result.left, node7)
        self.assertEqual(result.right, node2)
        self.assertEqual(result.left.left, node9)
        self.assertEqual(result.left.right, node6)
        self.assertEqual(result.right.left, node3)
        self.assertEqual(result.right.right, node1)
        print('Success: test_invert_tree')


def main():
    test = TestInvertTree()
    test.test_invert_tree()


if __name__ == '__main__':
    main()
