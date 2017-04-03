import sys


class PriorityQueueNode(object):

    def __init__(self, obj, key):
        self.obj = obj
        self.key = key

    def __repr__(self):
        return str(self.obj) + ': ' + str(self.key)


class PriorityQueue(object):

    def __init__(self):
        self.queue = []

    def insert(self, node):
        if node is not None:
            self.queue.append(node)
            return self.queue[-1]
        return None

    def extract_min(self):
        if not self.queue:
            return None
        minimum = sys.maxsize
        for index, node in enumerate(self.queue):
            if node.key < minimum:
                minimum = node.key
                minimum_index = index
        node = self.queue.pop(minimum_index)
        return node.obj

    def decrease_key(self, obj, new_key):
        for node in self.queue:
            if node.obj is obj:
                node.key = new_key
                return node
        return None