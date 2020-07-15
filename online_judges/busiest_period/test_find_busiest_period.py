import unittest


class TestSolution(unittest.TestCase):

    def test_find_busiest_period(self):
        solution = Solution()
        self.assertRaises(TypeError, solution.find_busiest_period, None)
        self.assertEqual(solution.find_busiest_period([]), None)
        data = [
            Data(3, 2, EventType.EXIT),
            Data(1, 2, EventType.ENTER),
            Data(3, 1, EventType.ENTER),
            Data(7, 3, EventType.ENTER),
            Data(9, 2, EventType.EXIT),
            Data(8, 2, EventType.EXIT),
        ]
        self.assertEqual(solution.find_busiest_period(data), Period(7, 8))
        print('Success: test_find_busiest_period')


def main():
    test = TestSolution()
    test.test_find_busiest_period()


if __name__ == '__main__':
    main()
