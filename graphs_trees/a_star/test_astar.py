
from unittest import TestCase


class TestAstar(TestCase):
    def test_astar_with_empty_board(self):
        board = []
        start = [0, 1]
        end = [3, 5]
        cost = 1  # cost is 1 per movement

        a_start = Astar()
        self.assertEqual(a_start.search(board=board, cost=cost, start=start, end=end), None)
        print('Success: test_astar_with_empty_board')

    def test_astar_with_valid_board(self):
        board = [
            [0, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 1],
            [0, 1, 0, 1, 0, 0],
            [0, 1, 0, 0, 1, 0],
            [0, 0, 0, 0, 1, 0],
        ]
        start = [0, 0]
        end = [3, 5]
        cost = 1  # cost is 1 per movement
        expected = [
            [0, -1, -1, -1, -1, -1],
            [1, 2, 3, 4, 5, -1],
            [-1, -1, -1, -1, 6, 7],
            [-1, -1, -1, -1, -1, 8],
            [-1, -1, -1, -1, -1, -1]
        ]

        a_start = Astar()
        self.assertEqual(a_start.search(board=board, cost=cost, start=start, end=end), expected)
        print('Success: test_astar_with_valid_board')

    def test_astar_with_another_valid_board(self):
        board = [
            [0, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 1],
            [0, 1, 0, 1, 0, 0],
            [0, 1, 0, 0, 1, 0],
            [0, 0, 0, 0, 1, 0],
        ]
        start = [0, 5]
        end = [4, 0]
        cost = 1  # cost is 1 per movement
        expected = [
            [-1, -1, -1, -1, 1, 0],
            [-1, -1, 4, 3, 2, -1],
            [-1, -1, 5, -1, -1, -1],
            [-1, -1, 6, -1, -1, -1],
            [9, 8, 7, -1, -1, -1]
        ]

        a_start = Astar()
        self.assertEqual(a_start.search(board=board, cost=cost, start=start, end=end), expected)
        print('Success: test_astar_with_another_valid_board')


    def test_astar_start_from_danger_zone(self):
        board = [
            [0, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 1],
            [0, 1, 0, 1, 0, 0],
            [0, 1, 0, 0, 1, 0],
            [0, 0, 0, 0, 1, 0],
        ]
        start = [0, 1]
        end = [3, 5]
        cost = 1  # cost is 1 per movement

        a_start = Astar()
        self.assertEqual(a_start.search(board=board, cost=cost, start=start, end=end), None)
        print('Success: test_astar_start_from_danger_zone')


    def test_astar_with_danger_zone_as_end(self):
        board = [
            [0, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 1],
            [0, 1, 0, 1, 0, 0],
            [0, 1, 0, 0, 1, 0],
            [0, 0, 0, 0, 1, 0],
        ]
        start = [0, 0]
        end = [2, 3]
        cost = 1
        expected = None

        a_start = Astar()
        self.assertEqual(a_start.search(board=board, cost=cost, start=start, end=end), expected)
        print('Success: test_astar_with_danger_zone_as_end')


def main():
    test = TestAstar()
    test.test_astar_with_empty_board()
    test.test_astar_with_valid_board()
    test.test_astar_with_another_valid_board()
    test.test_astar_start_from_danger_zone()
    test.test_astar_with_danger_zone_as_end()


if __name__ == '__main__':
    main()
