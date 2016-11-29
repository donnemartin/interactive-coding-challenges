from nose.tools import assert_equal


class TestGraph(object):

    def create_graph(self):
        graph = Graph()
        for key in range(0, 6):
            graph.add_node(key)
        return graph

    def test_graph(self):
        graph = self.create_graph()
        graph.add_edge(0, 1, weight=5)
        graph.add_edge(0, 5, weight=2)
        graph.add_edge(1, 2, weight=3)
        graph.add_edge(2, 3, weight=4)
        graph.add_edge(3, 4, weight=5)
        graph.add_edge(3, 5, weight=6)
        graph.add_edge(4, 0, weight=7)
        graph.add_edge(5, 4, weight=8)
        graph.add_edge(5, 2, weight=9)

        assert_equal(graph.nodes[0].adj_weights[graph.nodes[1].key], 5)
        assert_equal(graph.nodes[0].adj_weights[graph.nodes[5].key], 2)
        assert_equal(graph.nodes[1].adj_weights[graph.nodes[2].key], 3)
        assert_equal(graph.nodes[2].adj_weights[graph.nodes[3].key], 4)
        assert_equal(graph.nodes[3].adj_weights[graph.nodes[4].key], 5)
        assert_equal(graph.nodes[3].adj_weights[graph.nodes[5].key], 6)
        assert_equal(graph.nodes[4].adj_weights[graph.nodes[0].key], 7)
        assert_equal(graph.nodes[5].adj_weights[graph.nodes[4].key], 8)
        assert_equal(graph.nodes[5].adj_weights[graph.nodes[2].key], 9)

        assert_equal(graph.nodes[0].incoming_edges, 1)
        assert_equal(graph.nodes[1].incoming_edges, 1)
        assert_equal(graph.nodes[2].incoming_edges, 2)
        assert_equal(graph.nodes[3].incoming_edges, 1)
        assert_equal(graph.nodes[4].incoming_edges, 2)
        assert_equal(graph.nodes[5].incoming_edges, 2)

        graph.nodes[0].remove_neighbor(graph.nodes[1])
        assert_equal(graph.nodes[1].incoming_edges, 0)
        graph.nodes[3].remove_neighbor(graph.nodes[4])
        assert_equal(graph.nodes[4].incoming_edges, 1)

        assert_equal(graph.nodes[0] < graph.nodes[1], True)

        print('Success: test_graph')

    def test_graph_undirected(self):
        graph = self.create_graph()
        graph.add_undirected_edge(0, 1, weight=5)
        graph.add_undirected_edge(0, 5, weight=2)
        graph.add_undirected_edge(1, 2, weight=3)

        assert_equal(graph.nodes[0].adj_weights[graph.nodes[1].key], 5)
        assert_equal(graph.nodes[1].adj_weights[graph.nodes[0].key], 5)
        assert_equal(graph.nodes[0].adj_weights[graph.nodes[5].key], 2)
        assert_equal(graph.nodes[5].adj_weights[graph.nodes[0].key], 2)
        assert_equal(graph.nodes[1].adj_weights[graph.nodes[2].key], 3)
        assert_equal(graph.nodes[2].adj_weights[graph.nodes[1].key], 3)

        print('Success: test_graph_undirected')


def main():
    test = TestGraph()
    test.test_graph()
    test.test_graph_undirected()


if __name__ == '__main__':
    main()