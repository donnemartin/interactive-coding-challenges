# Python 2 users: Run pip install enum34
from enum import Enum


class State(Enum):
    unvisited = 1
    visited = 2
    visiting = 3


class Node:

    def __init__(self, id):
        self.id = id
        self.state = State.unvisited
        self.connections = {}


class Graph:

    def __init__(self):
        self.nodes = {}

    def add_node(self, id):
        node = Node(id)
        self.nodes[id] = node
        return node

    def add_edge(self, source, dest, weight=0):
        if source not in self.nodes:
            self.add_node(source)
        if dest not in self.nodes:
            self.add_node(dest)
        self.nodes[source].connections[self.nodes[dest]] = weight
