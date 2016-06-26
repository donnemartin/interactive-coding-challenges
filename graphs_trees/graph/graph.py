from enum import Enum  # Python 2 users: Run pip install enum34


class State(Enum):
    unvisited = 0
    visiting = 1
    visited = 2


class Node:

    def __init__(self, id):
        self.id = id
        self.visit_state = State.unvisited
        self.adjacent = {}  # key = node, val = weight

    def __str__(self):
        return str(self.id)

    def add_neighbor(self, neighbor, weight=0):
        self.adjacent[neighbor] = weight


class Graph:

    def __init__(self):
        self.nodes = {}  # key = node id, val = node

    def add_node(self, id):
        node = Node(id)
        self.nodes[id] = node
        return node

    def add_edge(self, id_source, id_dest, weight=0):
        if id_source not in self.nodes:
            self.add_node(id_source)
        if id_dest not in self.nodes:
            self.add_node(id_dest)
        self.nodes[id_source].add_neighbor(self.nodes[id_dest], weight)

    def add_undirected_edge(self, source, dest, weight=0):
        self.add_edge(source, dest, weight)
        self.nodes[dest].add_neighbor(self.nodes[source], weight)