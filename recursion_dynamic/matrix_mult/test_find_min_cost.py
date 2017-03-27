from nose.tools import assert_equal, assert_raises


class TestMatrixMultiplicationCost(object):

    def test_find_min_cost(self):
        matrix_mult_cost = MatrixMultiplicationCost()
        assert_raises(TypeError, matrix_mult_cost.find_min_cost, None)
        assert_equal(matrix_mult_cost.find_min_cost([]), 0)
        matrices = [Matrix(2, 3),
                    Matrix(3, 6),
                    Matrix(6, 4),
                    Matrix(4, 5)]
        expected_cost = 124
        assert_equal(matrix_mult_cost.find_min_cost(matrices), expected_cost)
        print('Success: test_find_min_cost')


def main():
    test = TestMatrixMultiplicationCost()
    test.test_find_min_cost()


if __name__ == '__main__':
    main()