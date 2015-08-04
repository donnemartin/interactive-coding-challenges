from nose.tools import assert_equal


class TestGraph(object):

    def test_graph(self):
        graph = Graph()
        for id in range(0, 6):
            graph.add_node(id)
        graph.add_edge(0, 1, 5)
        graph.add_edge(0, 5, 2)
        graph.add_edge(1, 2, 3)
        graph.add_edge(2, 3, 4)
        graph.add_edge(3, 4, 5)
        graph.add_edge(3, 5, 6)
        graph.add_edge(4, 0, 7)
        graph.add_edge(5, 4, 8)
        graph.add_edge(5, 2, 9)

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


def main():
    test = TestGraph()
    test.test_graph()


if __name__ == '__main__':
    main()