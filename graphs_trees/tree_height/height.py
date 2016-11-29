class BstHeight(Bst):

    def height(self, node):
        if node is None:
            return 0
        return 1 + max(self.height(node.left),
                       self.height(node.right))