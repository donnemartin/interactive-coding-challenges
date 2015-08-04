from collections import OrderedDict


class Node:

    def __init__(self, id):
        self.id = id
        self.visited = False
        self.adjacent = OrderedDict()  # key = node, val = weight


class Graph:

    def __init__(self):
        self.nodes = OrderedDict()  # key = node id, val = node

    def add_node(self, id):
        node = Node(id)
        self.nodes[id] = node
        return node

    def add_edge(self, source, dest, weight=0):
        if source not in self.nodes:
            self.add_node(source)
        if dest not in self.nodes:
            self.add_node(dest)
        self.nodes[source].adjacent[self.nodes[dest]] = weight