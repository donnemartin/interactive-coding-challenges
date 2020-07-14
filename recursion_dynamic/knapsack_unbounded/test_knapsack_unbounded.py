import unittest


class TestKnapsack(unittest.TestCase):

    def test_knapsack(self):
        knapsack = Knapsack()
        self.assertRaises(TypeError, knapsack.fill_knapsack, None, None)
        self.assertEqual(knapsack.fill_knapsack(0, 0), 0)
        items = []
        items.append(Item(label='a', value=1, weight=1))
        items.append(Item(label='b', value=3, weight=2))
        items.append(Item(label='c', value=7, weight=4))
        total_weight = 8
        expected_value = 14
        results = knapsack.fill_knapsack(items, total_weight)
        total_weight = 7
        expected_value = 11
        results = knapsack.fill_knapsack(items, total_weight)
        self.assertEqual(results, expected_value)
        print('Success: test_knapsack')

def main():
    test = TestKnapsack()
    test.test_knapsack()


if __name__ == '__main__':
    main()
