from nose.tools import assert_equal


class TestGraph(object):

    def create_graph(self):
        graph = Graph()
        for id in range(0, 6):
            graph.add_node(id)
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

        assert_equal(graph.nodes[0].adjacent[graph.nodes[1]], 5)
        assert_equal(graph.nodes[0].adjacent[graph.nodes[5]], 2)
        assert_equal(graph.nodes[1].adjacent[graph.nodes[2]], 3)
        assert_equal(graph.nodes[2].adjacent[graph.nodes[3]], 4)
        assert_equal(graph.nodes[3].adjacent[graph.nodes[4]], 5)
        assert_equal(graph.nodes[3].adjacent[graph.nodes[5]], 6)
        assert_equal(graph.nodes[4].adjacent[graph.nodes[0]], 7)
        assert_equal(graph.nodes[5].adjacent[graph.nodes[4]], 8)
        assert_equal(graph.nodes[5].adjacent[graph.nodes[2]], 9)

        print('Success: test_graph')

    def test_graph_undirected(self):
        graph = self.create_graph()

        graph.add_undirected_edge(0, 1, weight=5)
        graph.add_undirected_edge(0, 5, weight=2)
        graph.add_undirected_edge(1, 2, weight=3)

        assert_equal(graph.nodes[0].adjacent[graph.nodes[1]], 5)
        assert_equal(graph.nodes[1].adjacent[graph.nodes[0]], 5)
        assert_equal(graph.nodes[0].adjacent[graph.nodes[5]], 2)
        assert_equal(graph.nodes[5].adjacent[graph.nodes[0]], 2)
        assert_equal(graph.nodes[1].adjacent[graph.nodes[2]], 3)
        assert_equal(graph.nodes[2].adjacent[graph.nodes[1]], 3)

        print('Success: test_graph')


def main():
    test = TestGraph()
    test.test_graph()
    test.test_graph_undirected()


if __name__ == '__main__':
    main()