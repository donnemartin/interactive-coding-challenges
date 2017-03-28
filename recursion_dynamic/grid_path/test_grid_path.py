from nose.tools import assert_equal


class TestGridPath(object):

    def test_grid_path(self):
        grid = Grid()
        assert_equal(grid.find_path(None), None)
        assert_equal(grid.find_path([[]]), None)
        max_rows = 8
        max_cols = 4
        matrix = [[1] * max_cols for _ in range(max_rows)]
        matrix[1][1] = 0
        matrix[2][2] = 0
        matrix[3][0] = 0
        matrix[4][2] = 0
        matrix[5][3] = 0
        matrix[6][1] = 0
        matrix[6][3] = 0
        matrix[7][1] = 0
        result = grid.find_path(matrix)
        expected = [(0, 0), (1, 0), (2, 0),
                    (2, 1), (3, 1), (4, 1),
                    (5, 1), (5, 2), (6, 2), 
                    (7, 2), (7, 3)]
        assert_equal(result, expected)
        matrix[7][2] = 0
        result = grid.find_path(matrix)
        assert_equal(result, None)
        print('Success: test_grid_path')


def main():
    test = TestGridPath()
    test.test_grid_path()


if __name__ == '__main__':
    main()