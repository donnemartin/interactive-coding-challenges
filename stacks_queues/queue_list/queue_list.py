class Node(object):

    def __init__(self, data):
        self.data = data
        self.next = None


class Queue(object):

    def __init__(self):
        self.first = None
        self.last = None

    def enqueue(self, data):
        node = Node(data)
        if self.first is None and self.last is None:
            self.first = node
            self.last = node
        else:
            self.last.next = node
            self.last = node

    def dequeue(self):
        # Empty list
        if self.first is None and self.last is None:
            return None
        data = self.first.data
        # Remove only element from a one element list
        if self.first == self.last:
            self.first = None
            self.last = None
        else:
            self.first = self.first.next
        return data