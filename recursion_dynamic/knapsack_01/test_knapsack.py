import unittest


class TestKnapsack(unittest.TestCase):

    def test_knapsack_bottom_up(self):
        knapsack = Knapsack()
        self.assertRaises(TypeError, knapsack.fill_knapsack, None, None)
        self.assertEqual(knapsack.fill_knapsack(0, 0), 0)
        items = []
        items.append(Item(label='a', value=2, weight=2))
        items.append(Item(label='b', value=4, weight=2))
        items.append(Item(label='c', value=6, weight=4))
        items.append(Item(label='d', value=9, weight=5))
        total_weight = 8
        expected_value = 13
        results = knapsack.fill_knapsack(items, total_weight)
        self.assertEqual(results[0].label, 'd')
        self.assertEqual(results[1].label, 'b')
        total_value = 0
        for item in results:
            total_value += item.value
        self.assertEqual(total_value, expected_value)
        print('Success: test_knapsack_bottom_up')

    def test_knapsack_top_down(self):
        knapsack = KnapsackTopDown()
        self.assertRaises(TypeError, knapsack.fill_knapsack, None, None)
        self.assertEqual(knapsack.fill_knapsack(0, 0), 0)
        items = []
        items.append(Item(label='a', value=2, weight=2))
        items.append(Item(label='b', value=4, weight=2))
        items.append(Item(label='c', value=6, weight=4))
        items.append(Item(label='d', value=9, weight=5))
        total_weight = 8
        expected_value = 13
        self.assertEqual(knapsack.fill_knapsack(items, total_weight), expected_value)
        print('Success: test_knapsack_top_down')

def main():
    test = TestKnapsack()
    test.test_knapsack_bottom_up()
    test.test_knapsack_top_down()


if __name__ == '__main__':
    main()
