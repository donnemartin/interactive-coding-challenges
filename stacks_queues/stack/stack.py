class Node(object):
    
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack(object):
    
    def __init__(self, top=None):
        self.top = top

    def push(self, data):
        node = Node(data)
        node.next = self.top
        self.top = node

    def pop(self):
        if self.top is not None:
            data = self.top.data
            self.top = self.top.next
            return data
        return None

    def peek(self):
        if self.top is not None:
            return self.top.data
        return None

    def is_empty(self):
        return self.peek() is None