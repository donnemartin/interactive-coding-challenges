class Node(object):

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None

    def __str__(self):
        return str(self.data)


def insert(root, data):
    # Constraint: Assume we are working with valid ints
    if root is None:
        root = Node(data)
        return root
    if data <= root.data:
        if root.left is None:
            root.left = insert(root.left, data)
            root.left.parent = root
            return root.left
        else:
            return insert(root.left, data)
    else:
        if root.right is None:
            root.right = insert(root.right, data)
            root.right.parent = root
            return root.right
        else:
            return insert(root.right, data)