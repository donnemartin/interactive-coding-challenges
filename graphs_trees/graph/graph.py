from enum import Enum  # Python 2 users: Run pip install enum34


class State(Enum):
    unvisited = 0
    visiting = 1
    visited = 2


class Node:

    def __init__(self, key):
        self.key = key
        self.visit_state = State.unvisited
        self.incoming_edges = 0
        self.adj_nodes = {}  # Key = key, val = Node
        self.adj_weights = {}  # Key = key, val = weight

    def __repr__(self):
        return str(self.key)

    def __lt__(self, other):
        return self.key < other.key

    def add_neighbor(self, neighbor, weight=0):
        if neighbor is None:
            raise Exception('Invalid neighbor')
        neighbor.incoming_edges += 1
        self.adj_weights[neighbor.key] = weight
        self.adj_nodes[neighbor.key] = neighbor

    def remove_neighbor(self, neighbor):
        if neighbor is None or neighbor.key not in self.adj_nodes:
            raise Exception('Invalid neighbor')
        neighbor.incoming_edges -= 1
        del self.adj_weights[neighbor.key]
        del self.adj_nodes[neighbor.key]


class Graph:

    def __init__(self):
        self.nodes = {}  # Key = key, val = Node

    def add_node(self, key):
        if key is None:
            raise Exception('Invalid key')
        if key in self.nodes:
            return self.nodes[key]
        self.nodes[key] = Node(key)
        return self.nodes[key]

    def add_edge(self, source_key, dest_key, weight=0):
        if source_key is None or dest_key is None:
            raise Exception('Invalid key')
        if source_key not in self.nodes:
            self.add_node(source_key)
        if dest_key not in self.nodes:
            self.add_node(dest_key)
        self.nodes[source_key].add_neighbor(self.nodes[dest_key],
                                            weight)

    def add_undirected_edge(self, source_key, dest_key, weight=0):
        if source_key is None or dest_key is None:
            raise Exception('Invalid key')
        self.add_edge(source_key, dest_key, weight)
        self.nodes[dest_key].add_neighbor(self.nodes[source_key],
                                          weight)