from nose.tools import assert_equal


class TestDfs(object):

    def __init__(self):
        self.results = Results()

    def test_dfs(self):
        nodes = []
        graph = GraphDfs()
        for id in range(0, 6):
            nodes.append(graph.add_node(id))
        graph.add_edge(0, 1, 5)
        graph.add_edge(0, 4, 3)
        graph.add_edge(0, 5, 2)
        graph.add_edge(1, 3, 5)
        graph.add_edge(1, 4, 4)
        graph.add_edge(2, 1, 6)
        graph.add_edge(3, 2, 7)
        graph.add_edge(3, 4, 8)
        graph.dfs(nodes[0], self.results.add_result)
        assert_equal(str(self.results), "[0, 1, 3, 2, 4, 5]")

        print('Success: test_dfs')


def main():
    test = TestDfs()
    test.test_dfs()


if __name__ == '__main__':
    main()