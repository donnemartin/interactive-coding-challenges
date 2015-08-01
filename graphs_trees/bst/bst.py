from collections import deque


class Node(object):

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data):
        if data <= self.data:
            if self.left is None:
                self.left = Node(data)
            else:
                self.left.insert(data)
        else:
            if self.right is None:
                self.right = Node(data)
            else:
                self.right.insert(data)

    def in_order_traversal(self, visit_func):
        if self.left is not None:
            self.left.in_order_traversal(visit_func)
        visit_func(self.data)
        if self.right is not None:
            self.right.in_order_traversal(visit_func)

    def pre_order_traversal(self, visit_func):
        visit_func(self.data)
        if self.left is not None:
            self.left.pre_order_traversal(visit_func)
        if self.right is not None:
            self.right.pre_order_traversal(visit_func)

    def post_order_traversal(self, visit_func):
        if self.left is not None:
            self.left.post_order_traversal(visit_func)
        if self.right is not None:
            self.right.post_order_traversal(visit_func)
        visit_func(self.data)

    def bfs(self, visit_func):
        queue = deque()
        queue.append(self)
        while len(queue) > 0:
            node = queue.popleft()
            visit_func(node.data)
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)