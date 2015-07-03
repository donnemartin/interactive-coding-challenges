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
        
        # Remove only element from a one element list
        elif self.first == self.last:
            data = self.first.data
            self.first = None
            self.last = None
            return data
        else:
            data = self.first.data
            self.first = self.first.next
            return data